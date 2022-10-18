import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///app.db', echo=False, pool_recycle=7200)

Session = sessionmaker(bind=engine)
Base = declarative_base()

Session.configure(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'credentials'

    id = Column(Integer, primary_key=True)
    login = Column(String)
    password = Column(String)

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __repr__(self):

        return "<User('%s','%s')>" % (self.login, self.password)


metadata = Base.metadata
metadata.create_all(engine)

