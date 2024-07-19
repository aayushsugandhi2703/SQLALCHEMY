from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///newdatabase.db', echo=True)

base = declarative_base()

class Info(base):
    __tablename__='info'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Session= sessionmaker(bind=engine)

base.metadata.create_all(engine)
