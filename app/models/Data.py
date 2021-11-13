from app.db import Base
from sqlalchemy import Column, Integer, String

class Data(Base):
    __tablename__ = 'batch_jobs'
    id = Column(Integer, primary_key=True)
    batch_number = Column(String(50), nullable=True)
    submitted_at = Column(String(50), nullable=True)
    nodes_used = Column(String(50), nullable=True)