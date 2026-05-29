-- 1. Find students enrolled in multiple courses

SELECT s.student_name,
       COUNT(e.course_id) AS total_courses
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.student_name
HAVING COUNT(e.course_id) > 1;


-- 2. Calculate total students in each course

SELECT c.course_name,
       COUNT(e.student_id) AS total_students
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;


-- 3. Find top enrolled course

SELECT c.course_name,
       COUNT(e.student_id) AS total_students
FROM courses c
JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name
ORDER BY total_students DESC
LIMIT 1;


-- 4. List students not enrolled in any course

SELECT s.student_name
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id
WHERE e.student_id IS NULL;


-- 5. Generate department-wise student count

SELECT department,
       COUNT(*) AS total_students
FROM students
GROUP BY department;
