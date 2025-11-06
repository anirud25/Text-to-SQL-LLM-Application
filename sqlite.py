import sqlite3

conn=sqlite3.connect('student.db')
cursor=conn.cursor()

table_info="""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY, 
    NAME VARCHAR(25),
    CLASS VARCHAR(26),
    SECTION VARCHAR(25));
"""

cursor.execute(table_info)


cursor.execute("INSERT INTO students (NAME, CLASS, SECTION) VALUES ('Alice', '10th Grade', 'A')")
cursor.execute("INSERT INTO students (NAME, CLASS, SECTION) VALUES ('Bob', '10th Grade', 'B')")
cursor.execute("INSERT INTO students (NAME, CLASS, SECTION) VALUES ('Charlie', '9th Grade', 'A')")

print("Data inserted successfully")
print("The printed records are: ")
# data = cursor.execute("SELECT * FROM students").fetchall()
# print(data)

data = cursor.execute("SELECT * from students")
for row in data:
    print(row)

conn.commit()
conn.close()
               