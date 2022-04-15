
import datetime
dt=datetime.datetime.now()
print("Current date and time:")
print(dt)

a=input("Enter your first Name:")
b=input("Enter your last name")
print(b+a)

values=input("Enter the number:")
l=values.split(',')
t=tuple(l)
print('list:',l)
print('tuple:',t)
