# models.py
from sqlalchemy import Column, Integer, String
from base import Base

class Info(Base):
    __tablename__ = 'info1'

    Sr_no = Column(Integer, autoincrement=True)
    onefusion_id = Column(String(36), primary_key=True)
    diameter = Column(Integer, default=0)
    height = Column(Integer, default=0)
    width = Column(Integer, default=0)
    onefusion_height = Column(Integer, default=0)
    onefusion_width = Column(Integer, default=0)
    parameter_height = Column(Integer, default=0)
    parameter_width = Column(Integer, default=0)
