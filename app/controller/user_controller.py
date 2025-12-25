
from fastapi import HTTPException
from datetime import datetime, timedelta
import random

from app.models import user_model
from app.utils.email import send_otp_email
from app.utils.security import hash_password, verify_password


# =========================
# REGISTER ADMIN (ONLY)
# =========================
def register_admin(data):
    if user_model.find_admin_by_email(data.email):
        raise HTTPException(status_code=400, detail="Admin already exists")

    hashed_password = hash_password(data.password)
    admin = user_model.create_admin(data.name, data.email, hashed_password)

    return {
        "message": "Admin registered successfully",
        "admin": {
            "id": admin[0],
            "name": admin[1],
            "email": admin[2],
            "role": admin[3],
        },
    }


# =========================
# LOGIN (ADMIN + EMPLOYEE)
# =========================
# def login(data):
#     user = user_model.find_user_by_email(data.email)
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid email or password")

#     if not verify_password(data.password, user[3]):
#         raise HTTPException(status_code=401, detail="Invalid email or password")

#     return {
#         "message": "Login successful",
#         "user": {
#             "id": user[0],
#             "name": user[1],
#             "email": user[2],
#             "role": user[4],
#         },
#     }
def login(data):
    user = user_model.find_user_by_email(data.email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not verify_password(data.password, user[3]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {
        "message": "Login successful",
        "id": user[0],
        "name": user[1],
        "email": user[2],
        "role": user[4],
    }


# =========================
# FORGOT PASSWORD (ADMIN + EMPLOYEE)
# =========================
def forgot_password(data):
    user = user_model.find_user_by_email(data.email)
    if not user:
        # Do NOT reveal whether email exists (security best practice)
        return {"message": "If the email exists, an OTP has been sent"}

    otp = str(random.randint(100000, 999999))
    expiry = datetime.utcnow() + timedelta(minutes=10)

    user_model.save_otp(data.email, otp, expiry)
    send_otp_email(data.email, otp)

    return {"message": "OTP sent successfully"}


# =========================
# VERIFY OTP
# =========================
def verify_otp(data):
    user = user_model.verify_otp(data.email, data.otp)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid or expired OTP")

    # Clear OTP after successful verification
    user_model.save_otp(data.email, None, None)

    return {
        "message": "OTP verified successfully",
        "role": user[4],
    }


# =========================
# RESET PASSWORD
# =========================
def reset_password(data):
    if data.newPassword != data.confirmPassword:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    user = user_model.find_user_by_email(data.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    hashed_password = hash_password(data.newPassword)
    user_model.update_password(data.email, hashed_password)

    return {"message": "Password reset successful"}
