from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine=create_engine('sqlite:///thesacco.db')
Base=declarative_base()

