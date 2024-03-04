import psycopg2
from psycopg2 import sql
from password import password

# Database connection parameters
db_config = {
    "dbname": "a3q1",
    "user": "postgres",
    "password": password,
    "host": "localhost"
}

def connect_db():
    """Connect to the PostgreSQL database server."""
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**db_config)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    print("Connection successful.")
    return conn

def getAllStudents():
    """Retrieve all student records from the database."""
    conn = connect_db()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT * FROM students ORDER BY student_id ASC;")
        print("The number of students: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
        conn.close()
    else:
        print("Failed to connect to the database.")

def addStudent(first_name, last_name, email, enrollment_date):
    """Insert a new student record into the database."""
    conn = connect_db()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                    (first_name, last_name, email, enrollment_date))
        conn.commit()
        print("New student added successfully.")
        cur.close()
        conn.close()
    else:
        print("Failed to connect to the database.")

def updateStudentEmail(student_id, new_email):
    """Update the email address of a specific student."""
    conn = connect_db()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("UPDATE students SET email = %s WHERE student_id = %s;",
                    (new_email, student_id))
        conn.commit()
        print("Student email updated successfully.")
        cur.close()
        conn.close()
    else:
        print("Failed to connect to the database.")

def deleteStudent(student_id):
    """Delete a student record from the database."""
    conn = connect_db()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
        conn.commit()
        print("Student deleted successfully.")
        cur.close()
        conn.close()
    else:
        print("Failed to connect to the database.")

if __name__ == "__main__":
    getAllStudents()
