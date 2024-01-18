from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Cofounders(Base):
    __tablename__ = 'cofounders'
    id = Column(Integer, primary_key=True)
    name  = Column(String)
    designation = Column(String)
    teams = relationship("Teams", back_populates='leads')


class Teams(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    team = Column(String)
    cofounder_id = Column(Integer, ForeignKey('cofounders.id'))
    leads = relationship("Cofounders", back_populates='teams')

def createdb():
    # Connect to the database
    engine = create_engine('postgresql://graphql:demotest@localhost/postgres')
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    createdb()
    

