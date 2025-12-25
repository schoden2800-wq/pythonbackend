# # from fastapi import APIRouter
# # from app.controller.user_controller import (
# #     register_admin,
# #     login,
# #     forgot_password,
# #     verify_otp,
# #     reset_password
# # )
# # from app.schemas.user_schema import (
# #     RegisterAdmin,
# #     Login,
# #     ForgotPassword,
# #     VerifyOtp,
# #     ResetPassword
# # )

# # router = APIRouter(prefix="/api")

# # @router.post("/login")
# # def login_route(data: Login):
# #     return login(data)

# # @router.post("/admin/register")
# # def register_admin_route(data: RegisterAdmin):
# #     return register_admin(data)

# # @router.post("/admin/forgot-password")
# # def forgot_password_route(data: ForgotPassword):
# #     return forgot_password(data)

# # @router.post("/admin/verify-otp")
# # def verify_otp_route(data: VerifyOtp):
# #     return verify_otp(data)

# # @router.post("/admin/reset-password")
# # def reset_password_route(data: ResetPassword):
# #     return reset_password(data)
# from fastapi import APIRouter
# from app.controller.user_controller import (
#     register_admin,
#     login,
#     forgot_password,
#     verify_otp,
#     reset_password
# )
# from app.schemas.user_schema import (
#     RegisterAdmin,
#     Login,
#     ForgotPassword,
#     VerifyOtp,
#     ResetPassword
# )

# router = APIRouter(prefix="/api")


# # =========================
# # AUTH (ADMIN + EMPLOYEE)
# # =========================
# @router.post("/login")
# def login_route(data: Login):
#     return login(data)

# @router.post("/forgot-password")
# def forgot_password_route(data: ForgotPassword):
#     return forgot_password(data)

# @router.post("/verify-otp")
# def verify_otp_route(data: VerifyOtp):
#     return verify_otp(data)

# @router.post("/reset-password")
# def reset_password_route(data: ResetPassword):
#     return reset_password(data)


# # =========================
# # ADMIN ONLY
# # =========================
# @router.post("/admin/register")
# def register_admin_route(data: RegisterAdmin):
#     return register_admin(data)
from fastapi import APIRouter
from app.controller.user_controller import (
    register_admin,
    login,
    forgot_password,
    verify_otp,
    reset_password
)
from app.schemas.user_schema import (
    RegisterAdmin,
    Login,
    ForgotPassword,
    VerifyOtp,
    ResetPassword
)

router = APIRouter(prefix="/api")


# =========================
# AUTH (ADMIN + EMPLOYEE)
# =========================
@router.post("/login")
def login_route(data: Login):
    return login(data)

@router.post("/forgot-password")
def forgot_password_route(data: ForgotPassword):
    return forgot_password(data)

@router.post("/verify-otp")
def verify_otp_route(data: VerifyOtp):
    return verify_otp(data)

@router.post("/reset-password")
def reset_password_route(data: ResetPassword):
    return reset_password(data)


# =========================
# ADMIN ONLY
# =========================
@router.post("/admin/register")
def register_admin_route(data: RegisterAdmin):
    return register_admin(data)
