from sqlalchemy import Column, Integer, String
from pydantic import BaseModel


class EmployeeOut(BaseModel):
    model_config = {
        "from_attributes": True,
    }
    id: int
    name: str
    email: str
    designation: str
    salary: float

class PercentageItem(BaseModel):
    model_config = {
        "from_attributes": True,
    }
    id: int
    name: str
    salary: float
    percentage: float


class SummaryOut(BaseModel):
    model_config = {
        "from_attributes": True,
    }
    operations: str
    result: float | None
    breakdown: list[PercentageItem] | None
    employee_count: int
    message: str | None

class ErrorOut(BaseModel):
    model_config = {
        "from_attributes": True,
    }
    detail: str