# from fastapi import APIRouter
# from app.schemas.user_schema import AddEmployee
# # from app.controller.employee_controller import add_employee
# from app.controller.employee_controller import (
#     add_employee,
#     get_all_employees,
#     get_employee_by_id,
#     delete_employee

    
# )

# router = APIRouter(
#     prefix="/api/admin",
#     tags=["Admin"]
# )

# @router.post("/add-employee")
# def add_employee_route(data: AddEmployee):
#     return add_employee(data)
# @router.get("/employees")
# def get_all_employees_route():
#     return get_all_employees()


# @router.get("/employee/{employee_id}")
# def get_employee_by_id_route(employee_id: int):
#     return get_employee_by_id(employee_id)

# @router.delete("/employee/{employee_id}")
# def delete_employee_route(employee_id: int):
#     return delete_employee(employee_id)
from fastapi import APIRouter
from app.schemas.user_schema import AddEmployee
from app.controller.employee_controller import (
    add_employee,
    get_all_employees,
    get_employee_by_id,
    delete_employee
)

# =========================
# ADMIN ROUTES
# =========================
admin_router = APIRouter(
    prefix="/api/admin",
    tags=["Admin"]
)

@admin_router.post("/employees")
def add_employee_route(data: AddEmployee):
    return add_employee(data)

@admin_router.get("/employees")
def get_all_employees_route():
    return get_all_employees()

@admin_router.delete("/employees/{employee_id}")
def delete_employee_route(employee_id: int):
    return delete_employee(employee_id)


# =========================
# GENERAL ROUTES
# (ADMIN + EMPLOYEE)
# =========================
employee_router = APIRouter(
    prefix="/api",
    tags=["Employee"]
)

@employee_router.get("/employees/{employee_id}")
def get_employee_by_id_route(employee_id: int):
    return get_employee_by_id(employee_id)
