from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from api.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department = Column(String, nullable=True)
    role = Column(String, nullable=True)
    date_joined = Column(DateTime(timezone=True), server_default=func.now())
