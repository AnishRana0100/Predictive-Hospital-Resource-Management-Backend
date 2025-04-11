from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    admission_date = Column(DateTime, nullable=False)
    department = Column(String, nullable=False)
    predicted_los = Column(Integer)  # Length of Stay in days
    bed_id = Column(Integer, ForeignKey('beds.id'))
    bed = relationship("Bed", back_populates="patient")

class Bed(Base):
    __tablename__ = 'beds'
    id = Column(Integer, primary_key=True, index=True)
    department = Column(String, nullable=False)
    bed_type = Column(String, nullable=False)
    status = Column(String, nullable=False)  # e.g., 'available', 'occupied', 'reserved'
    patient = relationship("Patient", back_populates="bed", uselist=False)

class ResourceUsage(Base):
    __tablename__ = 'resource_usage'
    id = Column(Integer, primary_key=True, index=True)
    resource_type = Column(String, nullable=False)  # e.g., 'doctor', 'nurse', 'ventilator'
    current_usage = Column(Integer, nullable=False)
    predicted_usage = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)

