class Employee:
    x = 10
    def func_msg(self):
        print('Welcome to Employee Class')
class Department(Employee):
    a = 250
    b = Employee.x + 22
    def func_message(self):
        print('Welcome to Department Class')
    def func_changed(self):
        print('New Value = ', Employee.x + 449)
emp = Employee()
print(emp.x)
emp.func_msg()
dept = Department()
print(dept.a)
print(dept.b)
dept.func_message()
dept.func_changed()

