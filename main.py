import os
import logging
from contextlib import asynccontextmanager
from typing import List


from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi.middleware.cors import CORSMiddleware 


import models, schema
from database import Base, engine, get_db
from services import VALID_OPERATORS, calculate_summary

logger = logging.getLogger("employee_api")



@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting the application")
    models.Base.metadata.create_all(bind=engine)
    yield
    logger.info("Shutting down the application")

app = FastAPI(title="Employee Management API", lifespan=lifespan)

origins = os.getenv("CORS_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def _fetch_employees(db: Session) -> List[models.Employee]:
    try:
        return db.query(models.Employee).all()
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error")


@app.get("/employees", response_model=List[schema.EmployeeOut])
def list_employees(db: Session = Depends(get_db)):
    employees = _fetch_employees(db)
    return employees


@app.get("api/employees/summary", response_model=schema.SummaryOut)
def salary_summary(operations: str, db: Session = Depends(get_db)):
    if operations not in VALID_OPERATORS:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid operation. Valid operations are: {', '.join(VALID_OPERATORS)}")

    employees = _fetch_employees(db)
    summary = calculate_summary(employees, operations)
    return summary

@app.get("/")
def read_root():
    return {"Hello": "World"}
