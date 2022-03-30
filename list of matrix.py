a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[5,6,7],[8,9,10],[11,12,13]]
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    print(i)
    for j in range(len(b[0])):
        print(j)
        for k in range(len(b)):
            print(k)



            c[i][j]+=a[i][k]*b[k][j]
print("result matrix")
for r in c:
    print(r)

#result matrix
[54, 60, 66]
[126, 141, 156]
[198, 222, 246]
