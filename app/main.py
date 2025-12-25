
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.user_routes import router as user_router
from app.routes.employee_routes import admin_router, employee_router

app = FastAPI()

# =========================
# CORS CONFIG (FINAL)
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",           # local Vite
        "http://127.0.0.1:5173",
        "https://your-frontend.onrender.com",  # future prod frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# ROUTES
# =========================
app.include_router(user_router)
app.include_router(admin_router)
app.include_router(employee_router)

@app.get("/")
def root():
    return {"message": "Server is running"}
