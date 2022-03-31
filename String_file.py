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

