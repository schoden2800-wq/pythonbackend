# # from fastapi import FastAPI
# # from app.routes.user_routes import router
# # from app.routes.employee_routes import router as employee_router


# # app = FastAPI()

# # app.include_router(router)
# # app.include_router(router)


# # @app.get("/")
# # def root():
# #     return {"message": "Server is running"}
# from fastapi import FastAPI
# from app.routes.user_routes import router as user_router
# from app.routes.employee_routes import router as employee_router

# app = FastAPI()

# app.include_router(user_router)
# app.include_router(employee_router)

# @app.get("/")
# def root():
#     return {"message": "Server is running"}
from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.employee_routes import router as employee_router

app = FastAPI()

# 👇 ADD PREFIXES
app.include_router(user_router, prefix="/api/admin", tags=["Admin"])
app.include_router(employee_router, prefix="/api/employee", tags=["Employee"])

@app.get("/")
def root():
    return {"message": "Server is running"}
