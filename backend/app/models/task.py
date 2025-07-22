from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255))
    priority = Column(Integer)
    expiry_date = Column(DateTime)
