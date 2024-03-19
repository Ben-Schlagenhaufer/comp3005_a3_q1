COMP3005 Assignment 3 Question 1

This project aims to implement a PostgreSQL database 
and an application that connects to this database 
to perform specific CRUD (Create, Read, Update, Delete) operations

**Video Demonstration link: **https://vimeo.com/924839800/15bf5c79a1?share=copy

To run this application:

Prerequisites:
- Python
- PostgreSQL
- psycopg2 library for python (pip install psycopg2-binary) to install

To Create Table (in cmd line):

CREATE DATABASE your_database_name;

\c your_database_name

CREATE TABLE students (
  student_id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  enrollment_date DATE
);

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');


Pull from **Master** branch
