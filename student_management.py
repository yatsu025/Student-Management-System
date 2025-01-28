import csv

# File Names
student_file = "student_data.csv"
user_file = "users.csv"

# Function to Register Admin/User
def register_user():
    with open(user_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        role = input("Enter Role (admin/user): ").lower()
        writer.writerow([username, password, role])
        print("User Registered Successfully!")

# Function to Login
def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    with open(user_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == username and row[1] == password:
                print(f"Login Successful! Welcome, {username} ({row[2]})")
                return row[2]  # Return role (admin/user)
    print("Invalid Credentials!")
    return None

# Function to Add Student
def add_student():
    with open(student_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        name = input("Enter Student Name: ")
        age = input("Enter Age: ")
        marks = input("Enter Marks: ")
        section = input("Enter a Section: ")
        writer.writerow([name, age, marks , section])
        print("Student Added Successfully!")

# Function to View Students
def view_students():
    try:
        with open(student_file, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No records found!")

# Function to Search Student
def search_student():
    search_name = input("Enter Student Name to Search: ")
    found = False
    with open(student_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == search_name:
                print("Student Found:", row)
                found = True
                break
    if not found:
        print("Student Not Found!")

# Function to Delete Student (Only Admin)
def delete_student():
    search_name = input("Enter Student Name to Delete: ")
    rows = []
    deleted = False
    with open(student_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] != search_name:
                rows.append(row)
            else:
                deleted = True
    if deleted:
        with open(student_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found!")

# Main Program
print("1. Register")
print("2. Login")
choice = input("Enter your choice: ")

if choice == "1":
    register_user()
elif choice == "2":
    role = login()
    if role:
        while True:
            print("\nStudent Management System")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            if role == "admin":
                print("4. Delete Student")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                add_student()
            elif choice == "2":
                view_students()
            elif choice == "3":
                search_student()
            elif choice == "4" and role == "admin":
                delete_student()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid Choice! Try again.")
else:
    print("Invalid Option!")