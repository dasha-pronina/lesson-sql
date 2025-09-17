from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, Boolean

Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    body = Column(String)
    is_active = Column(Boolean, default=False)
