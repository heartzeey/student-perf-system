import streamlit as st
import sqlite3, joblib, json

MODEL_PATH = "student_model.pkl"
SCHEMA_PATH = "feature_schema.json"
DB_PATH = "database.db"

st.set_page_config(page_title="Student Performance Management System")
st.title("🎓 Student Performance Management System")

# Load schema
with open(SCHEMA_PATH) as f:
    schema = json.load(f)

# DB init
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT, password TEXT, role TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, email TEXT, score REAL, prediction TEXT)''')
conn.commit()

# Login
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = c.execute("SELECT role FROM users WHERE email=? AND password=?", (email, password)).fetchone()
    if user:
        st.success(f"Logged in as {user[0]}")
    else:
        st.error("Invalid login.")

st.caption("Default Admin: admin@example.com / Admin123!")
