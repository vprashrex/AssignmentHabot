from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api import models, schemas, crud, auth, dependencies
from .database import engine, get_db
from fastapi_pagination import add_pagination, Page,paginate
from typing import Optional


router = APIRouter()

models.Base.metadata.create_all(bind=engine)

@router.post("/api/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)

@router.get("/api/employees/", response_model=Page[schemas.Employee])
def list_employees(
    department: str = None,
    role: str = None,
    db: Session = Depends(get_db)
):
    employees = crud.get_employees(db, department=department, role=role)
    return paginate(employees)

@router.get("/api/employees/{id}/", response_model=schemas.Employee)
def retrieve_employee(id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id=id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.put("/api/employees/{id}/", response_model=schemas.Employee)
def update_employee(id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.update_employee(db=db, employee_id=id, employee=employee)

@router.delete("/api/employees/{id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(id: int, db: Session = Depends(get_db)):
    crud.delete_employee(db=db, employee_id=id)
    return None

add_pagination(router)
