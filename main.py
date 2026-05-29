from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import models
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Course Management System")


@app.get("/")
def home():
    return {"message": "Student Course Management API Running"}


# ---------------- STUDENT MANAGEMENT ----------------

@app.post("/students")
def add_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    existing_student = db.query(models.Student).filter(
        models.Student.email == student.email
    ).first()

    if existing_student:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_student = models.Student(**student.dict())

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {"message": "Student added successfully", "student_id": new_student.student_id}


@app.get("/students")
def view_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()


@app.put("/students/{student_id}")
def update_student(student_id: int, student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(
        models.Student.student_id == student_id
    ).first()

    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")

    for key, value in student.dict(exclude_unset=True).items():
        setattr(db_student, key, value)

    db.commit()

    return {"message": "Student updated successfully"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(
        models.Student.student_id == student_id
    ).first()

    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(db_student)
    db.commit()

    return {"message": "Student deleted successfully"}


# ---------------- COURSE MANAGEMENT ----------------

@app.post("/courses")
def add_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    existing_course = db.query(models.Course).filter(
        models.Course.course_code == course.course_code
    ).first()

    if existing_course:
        raise HTTPException(status_code=400, detail="Course code already exists")

    new_course = models.Course(**course.dict())

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return {"message": "Course added successfully", "course_id": new_course.course_id}

@app.get("/courses")
def view_courses(db: Session = Depends(get_db)):
    return db.query(models.Course).all()

@app.put("/courses/{course_id}")
def update_course(course_id: int, course: schemas.CourseUpdate, db: Session = Depends(get_db)):
    db_course = db.query(models.Course).filter(
        models.Course.course_id == course_id
    ).first()

    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")

    for key, value in course.dict(exclude_unset=True).items():
        setattr(db_course, key, value)

    db.commit()

    return {"message": "Course updated successfully"}

@app.delete("/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = db.query(models.Course).filter(
        models.Course.course_id == course_id
    ).first()

    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")

    db.delete(db_course)
    db.commit()

    return {"message": "Course deleted successfully"}


# ---------------- ENROLLMENT MANAGEMENT ----------------

@app.post("/enroll")
def enroll_student(enrollment: schemas.EnrollmentCreate, db: Session = Depends(get_db)):

    student = db.query(models.Student).filter(
        models.Student.student_id == enrollment.student_id
    ).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    course = db.query(models.Course).filter(
        models.Course.course_id == enrollment.course_id
    ).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    duplicate = db.query(models.Enrollment).filter(
        models.Enrollment.student_id == enrollment.student_id,
        models.Enrollment.course_id == enrollment.course_id
    ).first()

    if duplicate:
        raise HTTPException(status_code=400, detail="Student already enrolled")

    new_enrollment = models.Enrollment(**enrollment.dict())

    db.add(new_enrollment)
    db.commit()

    return {"message": "Enrollment successful"}

@app.get("/enrollments")
def view_enrollments(db: Session = Depends(get_db)):
    return db.query(models.Enrollment).all()
