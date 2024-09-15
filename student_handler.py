import sqlite3
from sqlite3 import Error

# ==========================================================
# DATABASE CONNECTION
# ==========================================================
database_file = "school_database.db"
conn = sqlite3.connect(database_file)
c = conn.cursor()

# ==========================================================
# [-1] CREATE A STUDENT
# ==========================================================
def create_student(student_id, f_name, l_name):
    # [DEFINE] the SQL statement
    sql = '''
        INSERT 
        INTO student(student_id, f_name, l_name) 
        VALUES(?, ?, ?)
    '''

    # [DEFINE] Take given variables and put into array
    s_data = (student_id, f_name, l_name)

    with conn:
        # [EXECUTE] Execute the SQL statment
        c.execute(sql, s_data)
    
    print("Inserted Data: " + student_id + ', ' + f_name + ', ' + l_name)

# ==========================================================
# [L] SHOW COURSE LIST
# ==========================================================
def list_courses():
    # [DEFINE] the SQL statement
    sql = '''
        SELECT *
        FROM course
    '''
    
    with conn:
        # [EXECUTE] Execute the SQL statment -> Get the assciated rows 
        c.execute(sql)
        rows = c.fetchall()
    
    # [RETURN] the list of course
    return rows

# ==========================================================
# [E] ENROLL STUDENT
# ==========================================================
def enroll_student(student_id, course_id, course_name):
    # SQL statement
    sql = """
        INSERT 
        INTO enrolled(student_id, course_id, course_name)
        VALUES(?, ?, ?)
    """
    
    # Put passed variables into an array
    enroll = (student_id, course_id, course_name)

    with conn:
        # [EXECUTE] Execute the SQL statment
        c.execute(sql, enroll)

        print("Enrolled Student with ID " + student_id + " Into class " + course_name)

# ==========================================================
# [W] WITHDRAW STUDENT
# ==========================================================
def withdraw_student(student_id):
    # [DEFINE] SQL statement
    sql = '''
        DELETE
        FROM enrolled 
        WHERE student_id=:student_id;
    '''
    
    with conn:
        # [EXECUTE] Execute the SQL statment
        c.execute(sql, {'student_id': student_id})

    print("Withdrew Student with ID: " + student_id)
# ==========================================================
# [S] SEARCH COURSES
# ==========================================================
def search_course(query):
    # [DEFINE] SQL statement
    sql = """
        SELECT *
        FROM course 
        WHERE course_name 
        LIKE :query;
    """

    query = '%' + query + '%'

    with conn:
        # [EXECUTE] the SQL statment
        result = c.execute(sql, {'query': query})

    # [RETURN] the list of courses
    return result

# ==========================================================
# [M] MY CLASSES (VIEW STUDENT CLASSES)
# ==========================================================
def my_clases(student_id):
    # [DEFINE] the SQL statement
    sql = """
        SELECT * 
        FROM enrolled 
        WHERE student_id=:student_id;
    """

    with conn:
        # [EXECUTE] Execute the SQL statment -> Get the assciated rows 
        c.execute(sql, {'student_id': student_id})
        rows = c.fetchall()
    
    # [RETURN] the list of course
    return rows

# ==========================================================
# M A I N
# ==========================================================
def main():
    # [DISPLAY] The functions availabe to the user
    print("\n" + "~~~ COMMANDS ~~~~~~~~~~~~~~~~~~")
    print("L - LIST") #DONE
    print("E - ENROLL") #DONE
    print("W - WITHDRAW") #DONE
    print("S - SEARCH") #DONE
    print("M - MY CLASSES") #DONE
    print("X - EXIT") #DONE
    print("-1 - CREATE A STUDENT") #DONE
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n")


    while True:
        user_input = input("Enter Command: ")
        print("\n")

        # [L] - LIST
        if (user_input == "l" or user_input == "L"):
            print("You Chose: l \n")

            # Print the table of courses
            print("\n" + "=== Courses ====================")
            data = list_courses()
            for s in data:
                print(*s)
            print("================================" + "\n")

        # [E] - ENROLL
        elif (user_input == "e" or user_input == 'E'):
            print("You Chose: e - Enroll Student \n")

            class_name = ''
            student_id = input("Enter ID of student to Enroll: ")
            
            # Print the table of courses
            print("\n" + "=== These are the curent classes and their ids ====================")
            data = list_courses()
            for s in data:
                print(*s)
            print("================================" + "\n")

            # Get the class ID and student to enroll ID
            class_id = input("Enter ID of class to enroll into: ")
            print("\n")

            if (class_id == '10'):
                class_name = 'Geology'

            elif (class_id == '20'):
                class_name = 'English'

            elif (class_id == '30'):
                class_name = 'Architecture'

            elif (class_id == '40'):
                class_name = 'Biology'

            elif (class_id == '50'):
                class_name = 'Calculus'
            
            else:
                print("Invalid Class ID")
                class_name = ''

            # Valid class id..
            if (class_name != ''):
                enroll_student(student_id, class_id, class_name)

        # [W] - WITHDRAW
        elif (user_input == "w" or user_input == 'W'):
            print("You Chose: w - Withdraw Student \n")

            # Get the student id and sent to function
            student_id = input("Student ID to withdraw: ")
            withdraw_student(student_id)

        # [S] - SEARCH COURSES
        elif (user_input == "s" or user_input == 'S'):
            print("You Chose: s - Search Course \n")

            query = input("Enter a course name to query a search: ")
            
            # Print the table of courses
            print("\n" + "=== " + "Search Results for: " + query + " ====================")
            data = search_course(query)
            for s in data:
                print(*s)
            print("================================" + "\n")

        # [M] - MYCLASSES
        elif (user_input == "m" or user_input == 'M'):
            print("You Chose: m - My Classes \n")

            student_id = input("Enter Student ID: ")

            print("\n" + "=== MY Classes ====================")
            
            data = my_clases(student_id)
            for s in data:
                print(*s)

            print("================================" + "\n")

        # [X] - EXIT
        elif (user_input == "x" or user_input == 'X'):
            print("You Chose: x - Exit \n")
            print("Bye!")
            break
    
        # [-1] - CREATE USER
        elif (user_input == "-1"):
            print("You Chose: -1 \n")

            student_id = input("Create your student ID: ")
            f_name = input("Input your first name: ")
            l_name = input("Input your last name: ")
            
            create_student(student_id, f_name, l_name)

        # [?] UNKNOWN COMMAND
        else:
            print("Unknown Command.")
            break
        
# Run the Main Function
main()