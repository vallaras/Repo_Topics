
def matrix(m):
    count=1
    while count<=100:
        print(count,"x",m,"=",count*m)
        count+=1
list=matrix(2)
print(list)


a=int(input("Enter the value :"))
sum=0
for i in range(1,a+1):
    m=int(input("Enter the number:"))
    sum=sum+m
    print(sum)
print(sum)


n=5
for i in range(n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
for k in range(n,0,-1):
    for l in range(k):
        print("*",end=" ")
    print()

def add():
    str="Dominic savio"
    x= "School"
    return [str,x]
l=add()
print(l)

def add(num):
    total=0
    for i in num:
        total+=i
    return total
print(add((1,2,3,4,5)))

a=[1,2,3,4,5,6,7]
#print(len(a))
#a.append(2)
#a.extend('11')
#a.insert(2,1)
#a.pop(7)

print(a)

x=int(input("Enter the value:"))
a=[[3,4,5,6],[2,3,4,5],[7,8,9,10]]
for i in a:
    if x in a:
       print(a[x])

