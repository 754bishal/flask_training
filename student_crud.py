import psycopg2


def db_connection():
    DB_NAME="postgres"
    DB_USER="postgres.tvqpxjoafhesywrnccur"
    DB_PASSWORD="bishal206605" 
    DB_HOST="aws-0-ap-southeast-1.pooler.supabase.com"
    DB_PORT="5432"
    try:
        conn= psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        print(conn)
        return conn
    except Exception as e:
        print("Error connecting to database")
        return None

def create_table_teachers():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers(
            teacher_i SERIAL PRIMARY KEY,
            teacher_name VARCHAR(90) NOT NULL,
            age INT NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table teacher created")

def create_table_courses():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("""
                create table if not exists courses (
                course_id serial primary key,
                course_name varchar(100) not null,
                teacher_id int references teachers(teacher_id) on delete cascade,
                credits int not null)
                   """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table courses created")

def create_table_students():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("""
                create table if not exists student (
                student_id serial primary key,
                name varchar(100) not null,
                course_id int references courses (course_id) on delete cascade,
                age int not null)
                   """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table students created")
    
def create_table_enrollments():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS enrollments (
                enrollment_id SERIAL PRIMARY KEY,
                student_id INT REFERENCES student(student_id) ON DELETE CASCADE,
                course_id INT REFERENCES courses(course_id) ON DELETE CASCADE,
                grade VARCHAR(2) NOT NULL
                    );
                   """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table enrollemts created")

def insert_teachers(teacher_id, teacher_name, age):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO teachers(teacher_id, teacher_name, age) VALUES(%s, %s, %s)", (teacher_id, teacher_name, age))
    conn.commit()
    cursor.close()
    conn.close()
    print("Values inserted in table teachers")

def insert_courses(course_id, course_name, teacher_id, credits):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO courses(course_id, course_name, teacher_id, credits) VALUES(%s, %s, %s, %s)", (course_id, course_name, teacher_id, credits))
    conn.commit()
    cursor.close()
    conn.close()
    print("Values inserted in table courses")

def insert_students(student_id, name, course_id, age):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO student(student_id, name, course_id, age) VALUES(%s, %s, %s, %s)", (student_id, name, course_id, age))
    conn.commit()
    cursor.close()
    conn.close()
    print("Values inserted in table students")
    
def insert_enrollments(enrollment_id,student_id, course_id, grade):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO enrollments(enrollment_id,student_id, course_id, grade) VALUES(%s, %s, %s, %s)", (enrollment_id,student_id, course_id, grade))
    conn.commit()
    cursor.close()
    conn.close()
    print("Values inserted in table enrollments")

def alter_table_courses():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("ALTER TABLE courses ADD COLUMN teacher_id int references teachers(teacher_id) on delete cascade")
    conn.commit()
    cursor.close()
    conn.close()
    print("Table courses altered")

def update_courses(teacher_id ,course_id):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("UPDATE courses SET teacher_id=%s WHERE course_id=%s", (teacher_id ,course_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Values inserted in table courses")

if __name__=="__main__":
<<<<<<< HEAD
   update_courses(102, 502)
=======
   update_courses(102, 502)
>>>>>>> fbbfb65 (1commit)
