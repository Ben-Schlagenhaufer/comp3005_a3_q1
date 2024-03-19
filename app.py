import psycopg2

#connect_db() connects to the postGre database using the psycopg2 extension
def connect_db():
    return psycopg2.connect(
        dbname="comp3005_a3_q1",
        user="postgres",
        password="1234",
        host="localhost"
    )


# getAllStudents function
# Connect to database, then execute the sql querie to get all students
# Store students, and print the result
def getAllStudents():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    for student in students:
        print(student)
    cur.close()
    conn.close()


# addStudent function
# Connect to database, then execute the sql querie to insert a student given the parameters
def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, enrollment_date))
    conn.commit()
    cur.close()
    conn.close()


#updateStudentEmail function
# Connect to database, then execute the sql querie to update a student email given the parameters
def updateStudentEmail(student_id, new_email):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    conn.commit()
    cur.close()
    conn.close()


#deleteStudent function
# Connect to database, then execute the sql querie to delete a student given the parameters
def deleteStudent(student_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    cur.close()
    conn.close()


#Main function that displays options and allows calls to previous functions
def main():
    while True:
        print("\n--- Student Database Management ---")
        print("1. List all students")
        print("2. Add a new student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            getAllStudents()
        elif choice == '2':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
            print("Student added successfully.")
        elif choice == '3':
            student_id = int(input("Enter student ID to update their email: "))
            new_email = input("Enter new email: ")
            updateStudentEmail(student_id, new_email)
            print("Student's email updated successfully.")
        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            deleteStudent(student_id)
            print("Student deleted successfully.")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()