from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, Boolean, DateTime, func

Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    body = Column(String)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )  # готовые функции на языке sql
