from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///empdetail.db', echo=True)
Base = declarative_base()

class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Details(Base):

    __tablename__ = "details"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(String)
    company = Column(String)
    country = Column(String)
    employee_id = Column(Integer, ForeignKey("employee.id"))
      


# create tables
Base.metadata.create_all(engine)        