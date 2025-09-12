from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean

Base = declarative_base()

class Flight(Base):
    __tablename__ = 'flights'
    id = Column(Integer, primary_key=True)
    airline = Column(String(255), nullable=False)
    origin = Column(String(255), nullable=False)
    destination = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    is_active = Column(Boolean, nullable=False)

    def __repr__(self):
        return f'[id={self.id}, airline={self.airline}, origin={self.origin}, destination={self.destination}, price={self.price}]'