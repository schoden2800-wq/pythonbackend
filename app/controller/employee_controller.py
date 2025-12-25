
from fastapi import HTTPException
import secrets
import string

from app.models import user_model
from app.utils.security import hash_password
from app.utils.email import send_employee_credentials


# -------- ADD EMPLOYEE (ADMIN ONLY) --------
def add_employee(data):
    if user_model.find_user_by_email(data.email):
        raise HTTPException(status_code=400, detail="Employee already exists")

    # Generate random password
    plain_password = "".join(
        secrets.choice(string.ascii_letters + string.digits)
        for _ in range(8)
    )

    hashed_password = hash_password(plain_password)

    # CREATE employee with designation
    employee = user_model.create_employee(
        name=data.name,
        email=data.email,
        password=hashed_password,
        designation=data.designation
    )

    send_employee_credentials(data.email, plain_password)

    return {
        "message": "Employee added successfully",
        "employee": {
            "id": employee[0],
            "name": employee[1],
            "email": employee[2],
            "designation": employee[3],
            "role": employee[4]
        }
    }


# -------- GET ALL EMPLOYEES --------
def get_all_employees():
    employees = user_model.get_all_employees()

    return [
        {
            "id": emp[0],
            "name": emp[1],
            "email": emp[2],
            "designation": emp[3],
            "role": emp[4]
        }
        for emp in employees
    ]


# -------- GET EMPLOYEE BY ID --------
def get_employee_by_id(employee_id: int):
    employee = user_model.get_employee_by_id(employee_id)

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {
        "id": employee[0],
        "name": employee[1],
        "email": employee[2],
        "designation": employee[3],
        "role": employee[4]
    }


# -------- DELETE EMPLOYEE --------
def delete_employee(employee_id: int):
    deleted = user_model.delete_employee(employee_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {
        "message": "Employee deleted successfully",
        "employee_id": deleted[0]
    }
    # -------- UPDATE EMPLOYEE --------
def update_employee(employee_id: int, data):
    employee = user_model.update_employee(
        employee_id,
        data.name,
        data.email,
        data.designation
    )

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {
        "message": "Employee updated successfully",
        "employee": {
            "id": employee[0],
            "name": employee[1],
            "email": employee[2],
            "designation": employee[3],
            "role": employee[4]
        }
    }
