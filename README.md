# 🎓 Student Performance Management System

A Streamlit-based web application for managing student records and predicting academic performance.

## Features
- Admin login to manage teachers/students.
- Teacher panel to manage students and run predictions.
- SQLite database for persistence.
- ML model (student_model.pkl) used for predictions.

## Setup (Local)
1. Place your trained model as `student_model.pkl` in the project folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run app:
   ```bash
   streamlit run app.py
   ```

## Deployment (Streamlit Cloud)
- Push this repo to GitHub.
- Deploy on Streamlit Cloud.
- Ensure `student_model.pkl` is included.

## Default Admin
- Email: admin@example.com
- Password: Admin123!
