
from fastapi import HTTPException
from datetime import datetime, timedelta
import random

from app.models import user_model
from app.utils.email import send_otp_email
from app.utils.security import hash_password, verify_password


# -------- REGISTER ADMIN --------
def register_admin(data):
    if user_model.find_admin_by_email(data.email):
        raise HTTPException(400, "Admin already exists")

    hashed = hash_password(data.password)
    admin = user_model.create_admin(data.name, data.email, hashed)

    return {
        "message": "Admin registered successfully",
        "admin": {
            "id": admin[0],
            "name": admin[1],
            "email": admin[2],
            "role": admin[3]
        }
    }


# -------- LOGIN (ADMIN + EMPLOYEE) --------
def login(data):
    user = user_model.find_user_by_email(data.email)
    if not user:
        raise HTTPException(401, "User not found")

    if not verify_password(data.password, user[3]):
        raise HTTPException(401, "Invalid password")

    return {
        "message": "Login successful",
        "user": {
            "id": user[0],
            "name": user[1],
            "email": user[2],
            "role": user[4]
        }
    }


# -------- FORGOT PASSWORD --------
# def forgot_password(data):
#     user = user_model.find_user_by_email(data.email)
#     if not user:
#         raise HTTPException(404, "User not found")

#     otp = str(random.randint(100000, 999999))
#     expiry = datetime.now() + timedelta(minutes=10)

#     user_model.save_otp(data.email, otp, expiry)
#     send_otp_email(data.email, otp)

#     return {"message": "OTP sent successfully"}

# def forgot_password(data):
#     user = user_model.find_user_by_email(data.email)
#     if not user:
#         raise HTTPException(404, "User not found")

#     otp = str(random.randint(100000, 999999))
#     expiry = datetime.now() + timedelta(minutes=10)

#     user_model.save_otp(data.email, otp, expiry)

#     email_sent = send_otp_email(data.email, otp)
#     if not email_sent:
#         raise HTTPException(
#             status_code=500,
#             detail="Failed to send OTP email"
#         )

#     return {"message": "OTP sent successfully"}
def forgot_password(data):
    user = user_model.find_user_by_email(data.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    otp = str(random.randint(100000, 999999))
    expiry = datetime.now() + timedelta(minutes=10)

    user_model.save_otp(data.email, otp, expiry)

    # ✅ Just send email (it raises exception if it fails)
    send_otp_email(data.email, otp)

    return {"message": "OTP sent successfully"}
# -------- VERIFY OTP --------
def verify_otp(data):
    user = user_model.verify_otp(data.email, data.otp)
    if not user:
        raise HTTPException(400, "Invalid or expired OTP")

    user_model.save_otp(data.email, None, None)

    return {
        "message": "OTP verified. Proceed to reset password.",
        "role": user[4]
    }


# -------- RESET PASSWORD --------
def reset_password(data):
    if data.newPassword != data.confirmPassword:
        raise HTTPException(400, "Passwords do not match")

    user = user_model.find_user_by_email(data.email)
    if not user:
        raise HTTPException(404, "User not found")

    hashed = hash_password(data.newPassword)
    user_model.update_password(data.email, hashed)

    return {"message": "Password reset successful"}
