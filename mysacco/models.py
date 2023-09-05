from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy

engine=create_engine('sqlite:///thesacco.db')
Base=declarative_base()


class Sacco(Base):
    
    __tablename__='saccos'
    
    id= Column(Integer(), primary_key=True)
    name=Column(String())
    manager=Column(String())
    created_at=Column(DateTime(), server_default=func.now())
    updated_at=Column(DateTime(), onupdate=func.now())
    
    all_vehicles=relationship('Vehicle', backref=backref('its_sacco'))
    all_members=association_proxy('all_vehicles','its_owner', creator=lambda me: Vehicle(its_owner=me))
    
    def __repr__(self):
        return f"ID= {self.id} | "+\
               f"NAME= {self.name} | " +\
               f"MANAGER= {self.manager}"

class Vehicle(Base):
    
    __tablename__='vehicles'
    
    id= Column(Integer(), primary_key=True)
    type=Column(String())
    number_plate=Column(String())
    sacco_id=Column(Integer(), ForeignKey('saccos.id'))
    owner_id=Column(Integer(), ForeignKey('members.id'))
    created_at=Column(DateTime(), server_default=func.now())
    updated_at=Column(DateTime(), onupdate=func.now())
    
    def __repr__(self):
        return f"ID= {self.id} | "+\
               f"TYPE= {self.type} | " +\
               f"NUMBER_PLATE= {self.number_plate}"
    
    
class Member(Base):
    
    __tablename__='members'
    
    id= Column(Integer(), primary_key=True)
    first_name=Column(String())
    last_name=Column(String())
    created_at=Column(DateTime(), server_default=func.now())
    updated_at=Column(DateTime(), onupdate=func.now())
    
    all_vehicles=relationship('Vehicle', backref=backref('its_owner'))
    all_saccos=association_proxy('all_vehicles','its_sacco', creator=lambda sa: Vehicle(its_sacco=sa))

    
    def __repr__(self):
        return f"ID= {self.id} | "+\
               f"FIRST_NAME= {self.first_name} | " +\
               f"LAST_NAME= {self.last_name}"