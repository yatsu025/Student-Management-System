# Student Management System

This is a simple command-line **Student Management System** written in Python. It includes user authentication and role-based access, where users can register, log in, and perform actions on student data stored in CSV files. The system allows users to add, view, search, and delete student records, with the **admin** having the special ability to delete students.

## Features

- **User Registration & Login**: Users can register with a username, password, and role (admin or user) and log in to access the system.
- **Student Management**:
  - **Add Student**: Admin and user can add student details like name, age, and marks.
  - **View Students**: Admin and user can view the list of all students.
  - **Search Student**: Admin and user can search for students by their name.
  - **Delete Student**: Only admins can delete student records.

## Prerequisites

- Python 3.x
- `student_data.csv`: To store student records.
- `users.csv`: To store user credentials (username, password, and role).
