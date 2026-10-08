--Day 3 lab music.db

DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS lessons;

CREATE TABLE teachers (
  teacher_id INTEGER PRIMARY KEY,
  first_name  TEXT NOT NULL,
  last_name   TEXT NOT NULL,
  email       TEXT UNIQUE
);

CREATE TABLE students (
  student_id INTEGER PRIMARY KEY,
  teacher_id INTEGER NOT NULL,
  first_name  TEXT NOT NULL,
  last_name   TEXT NOT NULL,
  email       TEXT UNIQUE,
  FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

CREATE TABLE lessons (
  lesson_id INTEGER PRIMARY KEY,
  student_id INTEGER NOT NULL,
  lesson_date  TEXT NOT NULL,
  lesson_time   TEXT NOT NULL,  
  instrument   TEXT NOT NULL,
  room    TEXT NOT NULL,
  FOREIGN KEY (student_id) REFERENCES students(student_id)
);

