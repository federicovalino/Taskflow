from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255))
    priority = Column(Integer)
    expiry_date = Column(DateTime)
    users = relationship("UserTask", back_populates="task")
    status = relationship("StatusTask", back_populates="task")
