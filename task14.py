def fun():
    str="National highway"
    x="nh4"
    return[str,x]
list=fun()
print(list)

def sum(number):
    total=0
    for i in number:
        total+=i
    return total
print(sum((8,2)))

def number(multi):
    total=1
    for i in multi:
        total*=i
    return total
list=number((8,2,3,-1,7))
print(list)

#Result

['National highway', 'nh4']
10
-336
