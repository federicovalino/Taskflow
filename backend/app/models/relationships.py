from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.database import Base
from datetime import datetime

class StatusTask(Base):
    __tablename__ = "status_task"

    id_task = Column(Integer, ForeignKey("tasks.id"), primary_key=True)
    id_status = Column(Integer, ForeignKey("statuses.id"), primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    status = Column(String(100))  # Puedes ajustarlo según tu lógica

class UserTask(Base):
    __tablename__ = "user_task"

    id_task = Column(Integer, ForeignKey("tasks.id"), primary_key=True)
    id_user = Column(Integer, ForeignKey("users.id"), primary_key=True)
    date_of_assignment = Column(DateTime, default=datetime.utcnow)
