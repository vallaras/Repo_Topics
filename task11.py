
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

#Return
c_c:  2000  r_c  1500


