Paste the content below.
# Student Course Management System

## Objective

Build a backend application to manage Students, Courses, and Enrollments using FastAPI and SQLAlchemy.

---

## Tech Stack

- Python 3.x
- FastAPI
- SQLAlchemy
- Pydantic
- MySQL / SQLite
- Swagger Documentation

---

## Features

### Student Management

- Add Student
- View Students
- Update Student Details
- Delete Student

### Course Management

- Add Course
- View Courses
- Update Course
- Delete Course

### Enrollment Management

- Enroll Student in Course
- View Student Enrollments
- Prevent Duplicate Enrollment

### Additional Features

- Input Validation using Pydantic
- Proper Error Handling
- Swagger Documentation
- Clean Folder Structure

---

## Project Structure

```text
student_course_management/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── README.md
│
├── sql/
│   ├── schema.sql
│   └── report_queries.sql
│
└── postman_collection.json

Installation

Install required packages:

pip install -r requirements.txt

Run the application:

uvicorn main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs

Database Tables

Students
student_id
student_name
email
department

Courses

course_id
course_name
course_code

Enrollments

enrollment_id
student_id
course_id
enrollment_date

SQL Reports

Students enrolled in multiple courses

Find students taking more than one course.

Total students in each course

Calculate student count per course.

Top enrolled course

Find course with highest enrollments.

Students not enrolled in any course

Identify inactive students.

Department-wise student count

Generate department-wise report.

Explanation

I created three database tables: Students, Courses, and Enrollments.

Students and Courses have a many-to-many relationship, so I used the Enrollments table as a junction table.

For Student Management and Course Management, I implemented complete CRUD operations using FastAPI.

For Enrollment Management, I added validation to prevent duplicate enrollments and ensured that both Student and Course exist before enrollment.

I used SQLAlchemy models for database interaction and Pydantic schemas for input validation.

Swagger documentation is automatically available through FastAPI.

SQL queries were written separately to generate reports and analytics.

Submission Files
FastAPI Source Code
SQL Schema Script
SQL Report Queries
Postman Collection
README.md

