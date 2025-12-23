# # # # # import smtplib
# # # # # import os
# # # # # from email.message import EmailMessage

# # # # # def send_otp_email(email, otp):
# # # # #     msg = EmailMessage()
# # # # #     msg["Subject"] = "Password Reset OTP"
# # # # #     msg["From"] = os.getenv("EMAIL_USER")
# # # # #     msg["To"] = email
# # # # #     msg.set_content(f"Your OTP is {otp}. Valid for 10 minutes.")

# # # # #     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
# # # # #         server.login(
# # # # #             os.getenv("EMAIL_USER"),
# # # # #             os.getenv("EMAIL_PASS")
# # # # #         )
# # # # #         server.send_message(msg)

# # # # import smtplib
# # # # import os
# # # # from email.message import EmailMessage


# # # # # -------- OTP EMAIL --------
# # # # def send_otp_email(email: str, otp: str):
# # # #     msg = EmailMessage()
# # # #     msg["Subject"] = "Password Reset OTP"
# # # #     msg["From"] = os.getenv("EMAIL_USER")
# # # #     msg["To"] = email
# # # #     msg.set_content(
# # # #         f"Your OTP is {otp}. It is valid for 10 minutes."
# # # #     )

# # # #     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
# # # #         server.login(
# # # #             os.getenv("EMAIL_USER"),
# # # #             os.getenv("EMAIL_PASS")
# # # #         )
# # # #         server.send_message(msg)


# # # # # -------- EMPLOYEE CREDENTIALS EMAIL --------
# # # # def send_employee_credentials(email: str, password: str):
# # # #     msg = EmailMessage()
# # # #     msg["Subject"] = "Your Employee Account Credentials"
# # # #     msg["From"] = os.getenv("EMAIL_USER")
# # # #     msg["To"] = email

# # # #     msg.set_content(
# # # #         f"""
# # # # Hello,

# # # # Your employee account has been created successfully.

# # # # Login Email: {email}
# # # # Temporary Password: {password}

# # # # Please log in and change your password immediately.

# # # # Regards,
# # # # Admin Team
# # # # """
# # # #     )

# # # #     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
# # # #         server.login(
# # # #             os.getenv("EMAIL_USER"),
# # # #             os.getenv("EMAIL_PASS")
# # # #         )
# # # #         server.send_message(msg)
# # # import os
# # # import smtplib
# # # from email.message import EmailMessage
# # # from dotenv import load_dotenv

# # # load_dotenv()

# # # EMAIL_USER = os.getenv("EMAIL_USER")
# # # EMAIL_PASS = os.getenv("EMAIL_PASS")

# # # if not EMAIL_USER or not EMAIL_PASS:
# # #     raise RuntimeError("Email credentials not configured")


# # # # -------- OTP EMAIL --------
# # # def send_otp_email(email: str, otp: str) -> bool:
# # #     try:
# # #         msg = EmailMessage()
# # #         msg["Subject"] = "Password Reset OTP"
# # #         msg["From"] = EMAIL_USER
# # #         msg["To"] = email
# # #         msg.set_content(
# # #             f"Your OTP is {otp}. It is valid for 10 minutes."
# # #         )

# # #         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
# # #             server.login(EMAIL_USER, EMAIL_PASS)
# # #             server.send_message(msg)

# # #         print("OTP email sent")
# # #         return True

# # #     except Exception as e:
# # #         print("OTP email error:", e)
# # #         return False


# # # # -------- EMPLOYEE CREDENTIALS EMAIL --------
# # # def send_employee_credentials(email: str, password: str) -> bool:
# # #     try:
# # #         msg = EmailMessage()
# # #         msg["Subject"] = "Your Employee Account Credentials"
# # #         msg["From"] = EMAIL_USER
# # #         msg["To"] = email

# # #         msg.set_content(
# # #             f"""
# # # Hello,

# # # Your employee account has been created successfully.

# # # Login Email: {email}
# # # Temporary Password: {password}

# # # Please log in and change your password immediately.

# # # Regards,
# # # Admin Team
# # # """
# # #         )

# # #         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
# # #             server.login(EMAIL_USER, EMAIL_PASS)
# # #             server.send_message(msg)

# # #         print("Employee credentials email sent")
# # #         return True

# # #     except Exception as e:
# # #         print("Employee email error:", e)
# # #         return False
# # import os
# # import smtplib
# # from email.message import EmailMessage
# # from dotenv import load_dotenv

# # load_dotenv()

# # EMAIL_USER = os.getenv("EMAIL_USER")
# # EMAIL_PASS = os.getenv("EMAIL_PASS")

# # if not EMAIL_USER or not EMAIL_PASS:
# #     raise RuntimeError("Email credentials not configured")


# # # -------- OTP EMAIL --------
# # def send_otp_email(email: str, otp: str) -> bool:
# #     try:
# #         msg = EmailMessage()
# #         msg["Subject"] = "Password Reset OTP"
# #         msg["From"] = EMAIL_USER
# #         msg["To"] = email
# #         msg.set_content(
# #             f"Your OTP is {otp}. It is valid for 10 minutes."
# #         )

# #         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
# #             server.login(EMAIL_USER, EMAIL_PASS)
# #             server.send_message(msg)

# #         print("OTP email sent")
# #         return True

# #     except Exception as e:
# #         print("OTP email error:", e)
# #         return False


# # # -------- EMPLOYEE CREDENTIALS EMAIL --------
# # def send_employee_credentials(email: str, password: str) -> bool:
# #     try:
# #         msg = EmailMessage()
# #         msg["Subject"] = "Your Employee Account Credentials"
# #         msg["From"] = EMAIL_USER
# #         msg["To"] = email

# #         msg.set_content(
# #             f"""Hello,

# # Your employee account has been created successfully.

# # Login Email: {email}
# # Temporary Password: {password}

# # Please log in and change your password immediately.

# # Regards,
# # Admin Team
# # """
# #         )

# #         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
# #             server.login(EMAIL_USER, EMAIL_PASS)
# #             server.send_message(msg)

# #         print("Employee credentials email sent")
# #         return True

# #     except Exception as e:
# #         print("Employee email error:", e)
# #         return False
# import os
# import smtplib
# from email.message import EmailMessage
# from dotenv import load_dotenv
# from google.oauth2.credentials import Credentials
# from google.auth.transport.requests import Request

# load_dotenv()

# GMAIL_USER = os.getenv("GMAIL_USER")  # your full Gmail address
# GMAIL_CLIENT_ID = os.getenv("GMAIL_CLIENT_ID")
# GMAIL_CLIENT_SECRET = os.getenv("GMAIL_CLIENT_SECRET")
# GMAIL_REFRESH_TOKEN = os.getenv("GMAIL_REFRESH_TOKEN")
# REDIRECT_URI = os.getenv("REDIRECT_URI")

# if not GMAIL_USER:
#     raise RuntimeError("GMAIL_USER not configured")

# def get_access_token() -> str:
#     creds = Credentials(
#         token=None,
#         refresh_token=GMAIL_REFRESH_TOKEN,
#         token_uri="https://oauth2.googleapis.com/token",
#         client_id=GMAIL_CLIENT_ID,
#         client_secret=GMAIL_CLIENT_SECRET,
#         scopes=["https://www.googleapis.com/auth/gmail.send"],
#     )
#     # Refresh the access token
#     request = Request()
#     creds.refresh(request)
#     return creds.token

# # def send_with_oauth2(email: str, subject: str, body: str) -> bool:
# #     access_token = get_access_token()
# #     if not access_token:
# #         print("Failed to obtain access token")
# #         return False

# #     try:
# #         # Build the XOAUTH2 authentication string
# #         auth_string = (
# #             f"user={GMAIL_USER}\1auth=Bearer {access_token}\1\1"
# #         )
# #         msg = EmailMessage()
# #         msg["Subject"] = subject
# #         msg["From"] = GMAIL_USER
# #         msg["To"] = email
# #         msg.set_content(body)

# #         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
# #             server.ehlo()
# #             server.auth("XOAUTH2", auth_string)
# #             server.send_message(msg)

# #         print("Email sent via OAuth2")
# #         return True
# #     except Exception as e:
# #         print("OAuth2 email error:", e)
# #         return False
# def send_with_oauth2(email: str, subject: str, body: str) -> bool:
#     access_token = get_access_token()
#     if not access_token:
#         print("Failed to obtain access token")
#         return False

#     try:
#         auth_string = f"user={GMAIL_USER}\x01auth=Bearer {access_token}\x01\x01"

#         msg = EmailMessage()
#         msg["Subject"] = subject
#         msg["From"] = GMAIL_USER
#         msg["To"] = email
#         msg.set_content(body)

#         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#             server.ehlo()
#             server.docmd("AUTH", "XOAUTH2 " + auth_string.encode("utf-8").decode("utf-8"))
#             server.send_message(msg)

#         print("Email sent via OAuth2")
#         return True

#     except Exception as e:
#         print("OAuth2 email error:", e)
#         raise

# def send_otp_email(email: str, otp: str) -> bool:
#     return send_with_oauth2(
#         email,
#         "Password Reset OTP",
#         f"Your OTP is {otp}. It is valid for 10 minutes."
#     )

# def send_employee_credentials(email: str, password: str) -> bool:
#     body = f"""Hello,

# Your employee account has been created successfully.

# Login Email: {email}
# Temporary Password: {password}

# Please log in and change your password immediately.

# Regards,
# Admin Team
# """
#     return send_with_oauth2(email, "Your Employee Account Credentials", body)
import os
import base64
from email.mime.text import MIMEText
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from fastapi import HTTPException

load_dotenv()

# ===============================
# ENV VARIABLES
# ===============================
GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_CLIENT_ID = os.getenv("GMAIL_CLIENT_ID")
GMAIL_CLIENT_SECRET = os.getenv("GMAIL_CLIENT_SECRET")
GMAIL_REFRESH_TOKEN = os.getenv("GMAIL_REFRESH_TOKEN")

if not all([
    GMAIL_USER,
    GMAIL_CLIENT_ID,
    GMAIL_CLIENT_SECRET,
    GMAIL_REFRESH_TOKEN
]):
    raise RuntimeError("Gmail OAuth environment variables not configured")

# ===============================
# GMAIL SERVICE
# ===============================
def get_gmail_service():
    creds = Credentials(
        token=None,
        refresh_token=GMAIL_REFRESH_TOKEN,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=GMAIL_CLIENT_ID,
        client_secret=GMAIL_CLIENT_SECRET,
        scopes=["https://www.googleapis.com/auth/gmail.send"],
    )

    return build("gmail", "v1", credentials=creds)

# ===============================
# CORE EMAIL SENDER
# ===============================
def send_email(to_email: str, subject: str, body: str):
    try:
        service = get_gmail_service()

        message = MIMEText(body)
        message["to"] = to_email
        message["from"] = GMAIL_USER
        message["subject"] = subject

        raw_message = base64.urlsafe_b64encode(
            message.as_bytes()
        ).decode()

        service.users().messages().send(
            userId="me",
            body={"raw": raw_message}
        ).execute()

        print("✅ Email sent successfully")

    except Exception as e:
        print("❌ Gmail API error:", e)
        raise HTTPException(
            status_code=500,
            detail="Failed to send email"
        )

# ===============================
# OTP EMAIL
# ===============================
def send_otp_email(email: str, otp: str):
    body = f"""
Your OTP is: {otp}

This OTP is valid for 10 minutes.
If you did not request a password reset, please ignore this email.
"""
    send_email(email, "Password Reset OTP", body)

# ===============================
# EMPLOYEE CREDENTIALS EMAIL
# ===============================
def send_employee_credentials(email: str, password: str):
    body = f"""
Hello,

Your employee account has been created successfully.

Login Email: {email}
Temporary Password: {password}

Please log in and change your password immediately.

Regards,
Admin Team
"""
    send_email(email, "Your Employee Account Credentials", body)
