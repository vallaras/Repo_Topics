class teacher:
    a=20
    def func_msg(self):
        print("welcome to hello world")
class student(teacher):
    x=250
    y=teacher.a + 20
    def func_msg(self):
        print("welcome to python")
    def change_value(self):
        print("New value=",teacher.a +30)
opj=teacher()
opj.func_msg()
stu=student()
print(stu.x)
print(stu.y)
stu.change_value()


class num:
    def __init__(self,fullname,emp_id,age):
        self.fullname=fullname
        self.emp_id=emp_id
        self.age=age
    def func_msg(self):
        print('At age',self.age,self.fullname,'is employee id',self.emp_id)
class math_fun(num):
    def __init__(self,fullname,emp_id,age):
        num.__init__(self,fullname,emp_id,age)
opj=num("valla",10,22)
opj.func_msg()
a=math_fun("ivana",11,18)
a.func_msg()

class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname


  def printname(self):
    print(self.fname, self.lname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("vallarasu", "M")
x.printname()
class num:
    def __init__(self,fullname,emp_id,age):
        self.fullname=fullname
        self.emp_id=emp_id
        self.age=age
    def func_msg(self):
        print('At age',self.age,self.fullname,'is employee id',self.emp_id)
class math_fun(num):
    def __init__(self,fullname,emp_id,age,department):
        num.__init__(self,fullname,emp_id,age)
        self.department=department
    def func_info(self):
        print('At age',self.age,self.fullname,'is employee id',self.emp_id,self.department)
opj=num("valla",10,22)
opj.func_msg()
a=math_fun("ivana","11","18","devloper")
a.func_info()
