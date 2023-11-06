from sqlalchemy import Column, Integer, String
from .database import Base

class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
