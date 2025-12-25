
# from app.config.database import get_cursor


# # -------- ADMIN --------
# def find_admin_by_email(email):
#     cur = get_cursor()
#     cur.execute(
#         "SELECT * FROM users WHERE email=%s AND role='admin'",
#         (email,)
#     )
#     return cur.fetchone()


# def create_admin(name, email, password):
#     cur = get_cursor()
#     cur.execute(
#         """
#         INSERT INTO users (name, email, password, role)
#         VALUES (%s, %s, %s, 'admin')
#         RETURNING id, name, email, role
#         """,
#         (name, email, password)
#     )
#     return cur.fetchone()


# # -------- EMPLOYEE --------
# def create_employee(name, email, password):
#     cur = get_cursor()
#     cur.execute(
#         """
#         INSERT INTO users (name, email, password, role)
#         VALUES (%s, %s, %s, 'employee')
#         RETURNING id, name, email, role
#         """,
#         (name, email, password)
#     )
#     return cur.fetchone()


# # -------- GENERIC --------
# def find_user_by_email(email):
#     cur = get_cursor()
#     cur.execute(
#         "SELECT * FROM users WHERE email=%s",
#         (email,)
#     )
#     return cur.fetchone()


# def save_otp(email, otp, expiry):
#     cur = get_cursor()
#     cur.execute(
#         """
#         UPDATE users
#         SET reset_otp=%s, reset_otp_expiry=%s
#         WHERE email=%s
#         """,
#         (otp, expiry, email)
#     )


# def verify_otp(email, otp):
#     cur = get_cursor()
#     cur.execute(
#         """
#         SELECT * FROM users
#         WHERE email=%s
#           AND reset_otp=%s
#           AND reset_otp_expiry > NOW()
#         """,
#         (email, otp)
#     )
#     return cur.fetchone()


# def update_password(email, password):
#     cur = get_cursor()
#     cur.execute(
#         """
#         UPDATE users
#         SET password=%s,
#             reset_otp=NULL,
#             reset_otp_expiry=NULL
#         WHERE email=%s
#         """,
#         (password, email)
#     )
# # -------- EMPLOYEE --------
# def get_all_employees():
#     cur = get_cursor()
#     cur.execute(
#         """
#         SELECT id, name, email, role
#         FROM users
#         WHERE role = 'employee'
#         ORDER BY id
#         """
#     )
#     return cur.fetchall()
# def get_employee_by_id(employee_id: int):
#     cur = get_cursor()
#     cur.execute(
#         """
#         SELECT id, name, email, role
#         FROM users
#         WHERE id = %s AND role = 'employee'
#         """,
#         (employee_id,)
#     )
#     return cur.fetchone()
# # -------- DELETE EMPLOYEE --------
# def delete_employee(employee_id: int):
#     cur = get_cursor()
#     cur.execute(
#         """
#         DELETE FROM users
#         WHERE id = %s AND role = 'employee'
#         RETURNING id
#         """,
#         (employee_id,)
#     )
#     return cur.fetchone()
from app.config.database import get_cursor


# =========================
# ADMIN
# =========================
def find_admin_by_email(email):
    cur = get_cursor()
    cur.execute(
        "SELECT * FROM users WHERE email=%s AND role='admin'",
        (email,)
    )
    return cur.fetchone()


def create_admin(name, email, password):
    cur = get_cursor()
    cur.execute(
        """
        INSERT INTO users (name, email, password, role)
        VALUES (%s, %s, %s, 'admin')
        RETURNING id, name, email, role
        """,
        (name, email, password)
    )
    return cur.fetchone()


# =========================
# EMPLOYEE
# =========================
def create_employee(name, email, password, designation):
    cur = get_cursor()
    cur.execute(
        """
        INSERT INTO users (name, email, password, designation, role)
        VALUES (%s, %s, %s, %s, 'employee')
        RETURNING id, name, email, designation, role
        """,
        (name, email, password, designation)
    )
    return cur.fetchone()


# =========================
# GENERIC
# =========================
def find_user_by_email(email):
    cur = get_cursor()
    cur.execute(
        "SELECT * FROM users WHERE email=%s",
        (email,)
    )
    return cur.fetchone()


def save_otp(email, otp, expiry):
    cur = get_cursor()
    cur.execute(
        """
        UPDATE users
        SET reset_otp=%s, reset_otp_expiry=%s
        WHERE email=%s
        """,
        (otp, expiry, email)
    )


def verify_otp(email, otp):
    cur = get_cursor()
    cur.execute(
        """
        SELECT * FROM users
        WHERE email=%s
          AND reset_otp=%s
          AND reset_otp_expiry > NOW()
        """,
        (email, otp)
    )
    return cur.fetchone()


def update_password(email, password):
    cur = get_cursor()
    cur.execute(
        """
        UPDATE users
        SET password=%s,
            reset_otp=NULL,
            reset_otp_expiry=NULL
        WHERE email=%s
        """,
        (password, email)
    )


# =========================
# EMPLOYEE QUERIES
# =========================
def get_all_employees():
    cur = get_cursor()
    cur.execute(
        """
        SELECT id, name, email, designation, role
        FROM users
        WHERE role = 'employee'
        ORDER BY id
        """
    )
    return cur.fetchall()


def get_employee_by_id(employee_id: int):
    cur = get_cursor()
    cur.execute(
        """
        SELECT id, name, email, designation, role
        FROM users
        WHERE id = %s AND role = 'employee'
        """,
        (employee_id,)
    )
    return cur.fetchone()


# =========================
# DELETE EMPLOYEE
# =========================
def delete_employee(employee_id: int):
    cur = get_cursor()
    cur.execute(
        """
        DELETE FROM users
        WHERE id = %s AND role = 'employee'
        RETURNING id
        """,
        (employee_id,)
    )
    return cur.fetchone()
