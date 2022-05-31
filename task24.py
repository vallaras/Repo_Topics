import sqlite3
stu_id = int(input("Enter the Student id: "))
stu_name = input("Enter the Student name: ")
stu_m1 = int(input("Enter the Student m1: "))
stu_m2 = int(input("Enter the Student m2: "))
stu_m3 = int(input("Enter the Student m3: "))
total = stu_m1 + stu_m2 + stu_m3
avg = total/3
if (stu_m1>=35 and stu_m2>=35 and stu_m3>=35):
    grade="Pass"
else:
    grade="Fail"
conn=sqlite3.connect(r'C:\Users\ELCOT\PycharmProjects\trining\student2.db')
cur=conn.cursor()
m=f"insert into student values({stu_id},'{stu_name}',{stu_m1},{stu_m2},{stu_m3},{total},{avg},'{grade}')"
print(m)
cur.execute('select * from Student')
cur.close()
conn.commit()
