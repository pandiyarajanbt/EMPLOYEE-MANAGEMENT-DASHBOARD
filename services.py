from decimal import ROUND_HALF_UP, Decimal
from typing import List
from models import Employee

VALID_OPERATORS = ["%", "max", "min", "avg", "sum"]
TWO_PLACES = Decimal("0.01")

def _q(value: Decimal) -> float:
    return float(Decimal(value).quantize(TWO_PLACES, rounding=ROUND_HALF_UP))



def calculate_summary(employees: List[Employee], operations: str) -> float:
    count = len(employees)
    if count == 0:
        return {
            "operations": operations,
            "result": None,
            "breakdown" : [] if operations == "%" else None,
            "employee_count": 0,
            "message": "No employees Records found"
        }

    salaries = [Decimal(str(e.salary)) for e in employees]
    total = sum(salaries)

    if operations == "%":
        breakdown = [
            {
            "id": e.id, 
            "name": e.name, 
            "salary": _q(s), 
            "percentage": _q((s / total) * 100) if total else 0,

            } for e, s in zip(employees, salaries)]

        return {"operations": operations, "result": None, "breakdown": breakdown, "employee_count": count,  "message": None}

    if operations == "max":
        result = max(salaries)
    elif operations == "min":
        result = min(salaries)
    elif operations == "avg":
        result = total / count
    else:
        result = total


    return {"operations": operations, "result": _q(result), "breakdown": None, "employee_count": count,  "message": None}
