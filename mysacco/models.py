from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine=create_engine('sqlite:///thesacco.db')
Base=declarative_base()


class Sacco(Base):
    
    __tablename__='saccos'
    
    id= Column(Integer(), primary_key=True)
    name=Column(String())
    manager=Column(String())
    created_at=Column(DateTime(), server_default=func.now())
    updated_at=Column(DateTime(), onupdate=func.now())

class Shuttle(Base):
    
    __tablename__='shuttles'
    
    id= Column(Integer(), primary_key=True)
    type=Column(String())
    number_plate=Column(String())
    created_at=Column(DateTime(), server_default=func.now())
    updated_at=Column(DateTime(), onupdate=func.now())
    
class Member(Base):
    
    __tablename__='members'
    
    id= Column(Integer(), primary_key=True)
    first_name=Column(String())
    last_name=Column(String())
    created_at=Column(DateTime(), server_default=func.now())
    updated_at=Column(DateTime(), onupdate=func.now())
