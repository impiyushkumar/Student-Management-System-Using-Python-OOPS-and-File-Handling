import string
import random
from pathlib import Path
import json


class Students:
    data = []
    count = 0 
    database = "students.json"

    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
                data = json.loads(fs.read())
                print("Data loaded from students.json")
    except Exception as err:
        print(f"Error loading file: {err}")

    @classmethod
    def randomid(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        dig = random.choices(string.digits, k=3)
        sym = random.choices("!@#$%^&*", k=2)
        q = alpha + dig + sym
        random.shuffle(q)
        return "".join(q)

    @classmethod
    def updateInfo(cls):
        try:
            with open(cls.database, 'w') as fs:
                fs.write(json.dumps(cls.data, indent=4))
            print("Data updated to students.json")
        except Exception as err:
            print(f"Error updating file: {err}")

    def registration(self):
        stu = {
            "id": Students.randomid(),
            "name": input("Enter name: "),
            "email": input("Enter email: "),
            "password": input("Enter password: "), 
            "skill": input("Enter skill: ")
        }
        Students.data.append(stu)
        Students.updateInfo()

    def readAllStudents(self):
        counter = 1
        for i in Students.data:
            print(f"\nStudent {counter}")
            for key, value in i.items():
                print(f"{key} -> {value}")
            counter += 1

    def readSingleStudent(self):
        search_id = input("Enter student ID to search: ")
        found = False
        for student in Students.data:
            if student['id'] == search_id:
                print(f"Student found: {student}")
                found = True
                break
        if not found:
            print(f"No student found with ID: {search_id}")

    def editStudentDetails(self):
        search_id = input("Enter student ID to edit: ")
        found = False
        for student in Students.data:
            if student['id'] == search_id:
                print(f"Editing details for student: {student['name']}")
                student['name'] = input(f"Enter new name ({student['name']}): ") or student['name']
                student['email'] = input(f"Enter new email ({student['email']}): ") or student['email']
                student['password'] = input(f"Enter new password ({student['password']}): ") or student['password']
                student['skill'] = input(f"Enter new skill ({student['skill']}): ") or student['skill']
                Students.updateInfo()
                print("Student details updated.")
                found = True
                break
        if not found:
            print(f"No student found with ID: {search_id}")

    def deleteStudent(self):
        search_id = input("Enter student ID to delete: ")
        found = False
        for student in Students.data:
            if student['id'] == search_id:
                Students.data.remove(student)
                Students.updateInfo()
                print(f"Student with ID {search_id} deleted.")
                found = True
                break
        if not found:
            print(f"No student found with ID: {search_id}")

student = Students()

while True:
    print("\nMenu:")
    print("1. Register a new student")
    print("2. View all student details")
    print("3. Read single student details")
    print("4. Edit student details")
    print("5. Delete a student")
    print("6. Exit")

    n = input("Please choose an option: ")

    if n == "1":
        student.registration()
    elif n == "2":
        student.readAllStudents()
    elif n == "3":
        student.readSingleStudent()
    elif n == "4":
        student.editStudentDetails()
    elif n == "5":
        student.deleteStudent()
    elif n == "6":
        break
    else:
        print("Invalid input. Please try again.")
