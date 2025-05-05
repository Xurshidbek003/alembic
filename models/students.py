from sqlalchemy import Column, Integer, String
from database_connect import Base


class Students(Base):

    __tablename__ = 'students'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(40), unique=True, nullable=False)
    address = Column(String(60), nullable=True)