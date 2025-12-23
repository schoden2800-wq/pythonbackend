# # # import psycopg2
# # # import os
# # # from dotenv import load_dotenv

# # # load_dotenv()

# # # conn = psycopg2.connect(
# # #     host=os.getenv("DB_HOST"),
# # #     user=os.getenv("DB_USER"),
# # #     password=os.getenv("DB_PASSWORD"),
# # #     database=os.getenv("DB_NAME"),
# # #     port=os.getenv("DB_PORT")
# # # )

# # # conn.autocommit = True

# # # def get_cursor():
# # #     return conn.cursor()
# # import psycopg2
# # import os
# # from dotenv import load_dotenv

# # load_dotenv()

# # conn = psycopg2.connect(
# #     host=os.getenv("DB_HOST"),
# #     user=os.getenv("DB_USER"),
# #     password=os.getenv("DB_PASSWORD"),
# #     database=os.getenv("DB_NAME"),
# #     port=os.getenv("DB_PORT")
# # )

# # conn.autocommit = True

# # def get_cursor():
# #     return conn.cursor()
# # import psycopg2
# # import os
# # from dotenv import load_dotenv

# # load_dotenv()

# # conn = psycopg2.connect(
# #     host=os.getenv("DB_HOST"),
# #     user=os.getenv("DB_USER"),
# #     password=os.getenv("DB_PASSWORD"),
# #     database=os.getenv("DB_NAME"),
# #     port=os.getenv("DB_PORT")
# # )

# # conn.autocommit = True

# # def get_cursor():
# #     return conn.cursor()
# import psycopg2
# import os
# from urllib.parse import urlparse

# DATABASE_URL = os.getenv("DATABASE_URL")

# if not DATABASE_URL:
#     raise RuntimeError("DATABASE_URL is not set")

# result = urlparse(DATABASE_URL)

# conn = psycopg2.connect(
#     database=result.path[1:],
#     user=result.username,
#     password=result.password,
#     host=result.hostname,
#     port=result.port,
#     sslmode="require"   # REQUIRED on Render
# )

# conn.autocommit = True

# def get_cursor():
#     return conn.cursor()
import psycopg2
import os
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

result = urlparse(DATABASE_URL)

# Detect local vs Render
is_local = result.hostname in ("localhost", "127.0.0.1")

conn = psycopg2.connect(
    database=result.path[1:],   # remove leading /
    user=result.username,
    password=result.password,
    host=result.hostname,
    port=result.port,
    sslmode="disable" if is_local else "require"
)

conn.autocommit = True

def get_cursor():
    return conn.cursor()
