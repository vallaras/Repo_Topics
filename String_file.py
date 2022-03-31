def myfun():
    a="hyundai multinational company"
    b="i20"
    return[a,b]
l=myfun()
print(l)


def myfun(a):
    ding = len(a)
    count = 0
    for char in a:
        count=count+1
    return count
print(myfun('TheNorthernLights   '))

def myfun(a):
  count=0
  for char in a:
    count=count+1
    return count
print(myfun("google"))

def mystring(a):
    if len(a)<2:
        return""
    return a[0:2]+a[-1]
print(mystring("sample10"))

arr1="apple"
arr2="classmate"
print(repr(arr1 and arr2))
print(repr(arr1 or arr2))
print(repr(not arr2))
print(repr(arr2 and arr1))
print(repr(arr2 or arr1))


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
