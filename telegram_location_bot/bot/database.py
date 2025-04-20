# database.py
import psycopg2
from datetime import datetime

# PostgreSQL connection
def connect_db():
    return psycopg2.connect(
        dbname="your_dbname",
        user="your_user",
        password="password",
        host="localhost",
        port="5432"
    )

def save_user_data(id, username, full_name, email="", phone_number="", status="active"):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Check if user already exists
        cursor.execute("SELECT 1 FROM users WHERE id = %s", (id,))
        if not cursor.fetchone():
            cursor.execute("""
                INSERT INTO users (id, username, full_name, email, phone_number, created_at, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (id, username, full_name, email, phone_number, datetime.now(), status))
            conn.commit()

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error while saving user: {e}")

def update_user_status(id, status):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("UPDATE users SET status = %s WHERE id = %s", (status, id))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error updating status: {e}")

def mark_user_inactive(id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE users SET status = 'inactive' WHERE id = %s
        """, (id,))
        conn.commit()

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error marking user inactive: {e}")

