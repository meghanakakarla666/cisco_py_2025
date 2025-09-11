from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean

Base = declarative_base()  #modal base classs

#models
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String(255),nullable=False)
    age = Column(Integer,nullable=False)
    salary = Column(Float,nullable=False)
    is_active = Column(Boolean,nullable=False)

    def __repr__(self):
        return f'[id={self.id}, name={self.name}, age={self.age},salary={self.salary}]'