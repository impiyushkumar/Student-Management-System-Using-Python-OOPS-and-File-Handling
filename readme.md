# Student Management System Using Python OOPS and File Handling

## Overview
The **Student Management System** is a Python-based application that allows users to manage student information using Object-Oriented Programming (OOP) principles and JSON file handling. This system supports functionalities like student registration, viewing all students, reading individual student details, editing student information, and deleting students.

## Features
- **Student Registration**: Add new students with unique ID, name, email, password, and skill.
- **View All Students**: Display all registered students with their details.
- **Read Single Student**: Search and display details of a student by their unique ID.
- **Edit Student Details**: Modify the details of an existing student.
- **Delete Student**: Remove a student from the system by their ID.
- **Persistent Data Storage**: Student data is stored in a JSON file, ensuring persistence between program runs.

## Technologies Used
- **Programming Language**: Python
- **File Handling**: JSON for storing and updating student data
- **OOP Concepts**: Classes, methods, class-level attributes

## Requirements
- Python 3.x
- `json` (part of Python Standard Library)
- `random` (part of Python Standard Library)
- `string` (part of Python Standard Library)
- `pathlib` (part of Python Standard Library)

## Usage
Upon running the program, a menu will be displayed, allowing the user to choose the following options:
1. **Register a new student**: Add a new student with a unique ID.
2. **View all student details**: List all registered students.
3. **Read single student details**: Find and display details of a specific student using their ID.
4. **Edit student details**: Update details of an existing student.
5. **Delete a student**: Remove a student from the system by their ID.
6. **Exit**: Close the program.

### Example
Here’s an example of how the registration process works:

```bash
Press 1 for registration:
Press 2 for details:
Press 3 to read single student:
Press 4 to edit details:
Press 5 to delete a user:
Press 6 to exit:

Please tell what you want to do: 1
Enter name: John Doe
Enter email: john@example.com
Enter password: mypassword123
Enter skill: Python
```

## Project Structure
```plaintext
.
├── students.json              # JSON file to store student data
├── student_management_system.py # Main Python script for the system
└── README.md                   # Project documentation
```

## Future Enhancements
- Add more fields such as course details or grades.
- Implement a GUI using a Python library like Tkinter or PyQt.
- Add password encryption for better security.


