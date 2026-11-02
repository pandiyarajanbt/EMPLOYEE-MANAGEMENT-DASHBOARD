from decimal import ROUND_HALF_UP, Decimal
from database import Base, SessionLocal, engine
from models import Employee

SAMPLE = [
    (1, "Rahul Sharma ", "rahul@example.com", "Software Engineer", Decimal("60000.00")),
    (2, "Priya Singh", "priya@example.com", "Data Analyst", Decimal("55000.00")),
    (3, "Amit Kumar", "amit@example.com", "Product Manager", Decimal("70000.00")),
    (4, "Sneha Patel", "sneha@example.com", "UX Designer", Decimal("65000.00")),
    (5, "Vikram Mehta", "vikram@example.com", "DevOps Engineer", Decimal("75000.00")),
    (6, "Neha Gupta", "neha@example.com", "Marketing Specialist", Decimal("50000.00")),
    (7, "Rajesh Verma", "rajesh@example.com", "Financial Analyst", Decimal("62000.00")),
    (8, "Pooja Reddy", "pooja@example.com", "HR Manager", Decimal("68000.00")),
    (9, "Suresh Iyer", "suresh@example.com", "Backend Developer", Decimal("72000.00")),
    (10, "Anjali Nair", "anjali@example.com", "Frontend Developer", Decimal("67000.00")),
]

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        for emp in SAMPLE:
            employee = Employee(id=emp[0], name=emp[1], email=emp[2], designation=emp[3], salary=emp[4])
            db.add(employee)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error seeding data: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed()