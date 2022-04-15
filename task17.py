
l=10000
h=3500
c_c=0
r_c=0
for i in range(0,(l//4)+1):
    for j in range(0,(l//2)+1):
        if h==i+j and l==i*4 + j*2:
                c_c=j
                r_c=i
if c_c==0 and r_c==0:
    print("legs and head count mismatch")
else:
    print("c_c: ",c_c ," r_c ", r_c)


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


#L=list(range(0,101))
for i in range(2,101,2):
    print('Even Number :',i)
for j in range(1,102,3):
    print('Odd Number:',j)

n=100
for i in range(n):
    if i%2==0:
        print("Even Number:",i)
    elif i%3==0:
        print("Odd Number:",i)
    #else:
        #print("No variable")


