from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class StatusTask(Base):
    __tablename__ = "status_task"

    id_task = Column(Integer, ForeignKey("tasks.id"), primary_key=True)
    id_status = Column(Integer, ForeignKey("status.id"), primary_key=True)
    date = Column(DateTime, default=datetime.now)
    status = Column(String(100)) 
    task = relationship("Task", back_populates="status")
    status_obj = relationship("Status", back_populates="tasks")

class UserTask(Base):
    __tablename__ = "user_task"

    id_task = Column(Integer, ForeignKey("tasks.id"), primary_key=True)
    id_user = Column(Integer, ForeignKey("users.id"), primary_key=True)
    date_of_assignment = Column(DateTime, default=datetime.now)
    user = relationship("User", back_populates="tasks")
    task = relationship("Task", back_populates="users")
