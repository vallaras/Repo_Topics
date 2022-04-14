def enumber(a):
    l=[]
    for i in a:
        if i%2==0:
            l.append(i)
    return l
print(enumber([1,2,3,4,5,6,7,8,9]))

n = 5
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')

#Result
[2, 4, 6, 8]

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
