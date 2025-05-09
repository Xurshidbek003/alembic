from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from database_connect import Base


class News(Base):

    __tablename__ = 'news'
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(50), nullable=False)
    text = Column(Text, nullable=False)
    created_at = Column(Date, nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    view = Column(Integer, nullable=False, default=0)


