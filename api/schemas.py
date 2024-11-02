from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    department: Optional[str]
    role: Optional[str]

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    date_joined: datetime  # Update to use datetime type

    class Config:
        orm_mode = True
        json_encoders = {datetime: lambda v: v.isoformat()}
