from sqlalchemy import Column, Integer, Text
from db.session import Base

class Note(Base):

    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
