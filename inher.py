class stage:
    y=230
    str1="search the word in the sentance"
    lis=str1.split(" ")
    res = []
    for i in range(0,len(lis)):
        for j in range(i+1,len(lis)):
            if lis[i]==lis[j] and lis[i] not in res:
                res.append(lis[i])
        def myfun_msg(self):
            print("two three zero")
class letter(stage):
    x=300
    def myfun_msg(self):
        print("welcome to python ")
        print("python easy to learn")
opj=stage()
print(opj.res)
print(opj.y)
opj.myfun_msg()
o=letter()
print(o.x)
o.myfun_msg()

#Result
['the']
230
two three zero
300
welcome to python 
python easy to learn
