from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Status(Base):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True, index=True)
    status_description = Column(String(100), nullable=False)
    tasks = relationship("StatusTask", back_populates="status_obj")
