from sqlalchemy import Text, Column, ForeignKey, Integer, String, DateTime, Date, JSON, Table
from sqlalchemy.orm import relationship, mapped_column
from database.connection import Base
from sqlalchemy.orm import Session
import time


class Books(Base):
    __tablename__ = "books"
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(Text)
    date_added = Column(DateTime)

