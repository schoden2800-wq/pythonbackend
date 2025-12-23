# from passlib.context import CryptContext

# pwd_context = CryptContext(
#     schemes=["bcrypt"],
#     deprecated="auto"
# )

# def hash_password(password: str) -> str:
#     password = password.strip()
#     return pwd_context.hash(password)

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     plain_password = plain_password.strip()

#     # bcrypt hard limit protection
#     if len(plain_password.encode("utf-8")) > 72:
#         return False

#     return pwd_context.verify(plain_password, hashed_password)
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    return pwd_context.hash(password.strip())

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password.strip(), hashed_password)
