from pydantic import BaseModel, EmailStr


class RegisterAdmin(BaseModel):
    name: str
    email: EmailStr
    password: str


class Login(BaseModel):
    email: EmailStr
    password: str


class ForgotPassword(BaseModel):
    email: EmailStr


class VerifyOtp(BaseModel):
    email: EmailStr
    otp: str


class ResetPassword(BaseModel):
    email: EmailStr
    newPassword: str
    confirmPassword: str


# ✅ ADD THIS (THIS IS WHAT WAS MISSING)
class AddEmployee(BaseModel):
    name: str
    email: EmailStr
    designation: str
class UpdateEmployee(BaseModel):
    name: str
    email: EmailStr
    designation: str