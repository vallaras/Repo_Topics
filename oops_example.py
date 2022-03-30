class Demo:
    print("class method")
    d=50
    def example(self,a,b):
        c=a+b+self.d
        return c

o=Demo()
ans=o.example(10,20)
print(ans)


class tr:
    course='python'
    def example(self):
        cn=self.course
        print(f"we are study{self.course}")
o1=tr()
print(o1.course)
o1.example()


class student:
    stu_id=100
    stu_name='vallarasu'
    def __init__(self):
        print('tranic constr')

    def printmessage(self):
            print(f"student id={self.stu_id}and name={self.stu_name}")
opj=student()
opj.printmessage()

class emplyee:
    emp_id=100
    emp_name='abc'
    emp_location='tambarm'
    emp_ph=9940571924
    def __init__(self):
        print('tranic consder')
    def printmessage(self):
        print(f"emplyee id={self.emp_id},name={self.emp_name},loction={self.emp_location},ph={self.emp_ph}")
opj=emplyee()
opj.printmessage()


#output
class method
80
python
we are studypython
tranic constr
student id=100and name=vallarasu
tranic consder
emplyee id=100,name=abc,loction=tambarm,ph=9940571924
