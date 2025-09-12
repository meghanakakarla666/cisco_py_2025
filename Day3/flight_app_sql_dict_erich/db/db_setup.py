from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .db_models import Base, Flight

engine = create_engine('sqlite:///flight_app_db.db', echo=True)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()