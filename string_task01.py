str1="teen"
lis=list(str1)
res=[]
for i in range(0,len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i]==lis[j] and lis[i] not in res:
            res.append(lis[i])

print(res)



str1="search the word in the sentance"
lis=str1.split(" ")
res=[]
for i in range(0,len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i]==lis[j] and lis[i] not in res:
            res.append(lis[i])

print(res)

#Result

['e']
['the']
