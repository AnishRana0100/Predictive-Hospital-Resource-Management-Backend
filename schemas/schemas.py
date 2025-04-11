from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PatientBase(BaseModel):
    name: str
    admission_date: datetime
    department: str
    predicted_los: Optional[int]

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    bed_id: Optional[int]

    class Config:
        orm_mode = True

class BedBase(BaseModel):
    department: str
    bed_type: str
    status: str

class BedCreate(BedBase):
    pass

class Bed(BedBase):
    id: int

    class Config:
        orm_mode = True

class ResourceUsageBase(BaseModel):
    resource_type: str
    current_usage: int
    predicted_usage: int
    date: datetime

class ResourceUsageCreate(ResourceUsageBase):
    pass

class ResourceUsage(ResourceUsageBase):
    id: int

    class Config:
        orm_mode = True

