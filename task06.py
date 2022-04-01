'''
counter = 1
while (counter<=100):
    print(counter,end="")
    counter+=1
    print()
'''
#Sample String : google.com
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
def myfun(a):
    d={}
    #a="google.com"
    for i in a:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    return d
    #b=[i.lower() for i in a]
    #print(b)
print(myfun("vallarasu"))



def string(a):
    d={}
    for i in a:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    return d
print(string("google.com"))


def myfun(a):
     if len(a)<2:
         print("")
     return a[0]+a[-1]
print(myfun("good"))

#Result
{'v': 1, 'a': 3, 'l': 2, 'r': 1, 's': 1, 'u': 1}
{'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
gd
