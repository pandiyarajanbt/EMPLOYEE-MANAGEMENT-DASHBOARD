from sqlalchemy import Column, Integer, String, Numeric
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    designation = Column(String, nullable=False)
    salary = Column(Numeric(10, 2), nullable=False)