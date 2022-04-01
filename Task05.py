
a=int(input("Enter the number:"))
for i in range(1,a+1):
    if (i%2==0):
        print(i)

count=1
while count<=5:
    print("welcome")
    count=count+1


def test(a):
    l=[]
    for i in a:
        l.append(i)
    return l
print(test((1,2,3,4,5,6,7,8,9,10)))


for k in range(1,10):
    for y in range(1,10):
        print(k*y,end="")
    print()


def test(a):
    for i in a:
        if (i%2==0):
            print(i)

print(test((1,2,3,4,5,6,7,8,9,10)))


for i in range(7):
    if (i==3 or i==6 or i==1):
        continue
    print(i,end="")
print()

#Expected Output : 1 1 2 3 5 8 13 21 34
def test(a):
    x,y=0,1
    for i in range(a):
        if i==1:
            x,y=y,x+y
            print(x,y)
    print(i,end="")
print(test(10))

n=int(input("Enter the number:"))
for i in range(1,101):
    print(i,'x',n,'=',i*n)

#Result
Enter the number:10
2
4
6
8
10
welcome
welcome
welcome
welcome
welcome
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
123456789
24681012141618
369121518212427
4812162024283236
51015202530354045
61218243036424854
71421283542495663
81624324048566472
91827364554637281
2
4
6
8
10
None
0245
1 1
9None
Enter the number:10
1 x 10 = 10
2 x 10 = 20
3 x 10 = 30
4 x 10 = 40
5 x 10 = 50
6 x 10 = 60
7 x 10 = 70
8 x 10 = 80
9 x 10 = 90
10 x 10 = 100
11 x 10 = 110
12 x 10 = 120
13 x 10 = 130
14 x 10 = 140
15 x 10 = 150
16 x 10 = 160
17 x 10 = 170
18 x 10 = 180
19 x 10 = 190
20 x 10 = 200
21 x 10 = 210
22 x 10 = 220
23 x 10 = 230
24 x 10 = 240
25 x 10 = 250
26 x 10 = 260
27 x 10 = 270
28 x 10 = 280
29 x 10 = 290
30 x 10 = 300
31 x 10 = 310
32 x 10 = 320
33 x 10 = 330
34 x 10 = 340
35 x 10 = 350
36 x 10 = 360
37 x 10 = 370
38 x 10 = 380
39 x 10 = 390
40 x 10 = 400
41 x 10 = 410
42 x 10 = 420
43 x 10 = 430
44 x 10 = 440
45 x 10 = 450
46 x 10 = 460
47 x 10 = 470
48 x 10 = 480
49 x 10 = 490
50 x 10 = 500
51 x 10 = 510
52 x 10 = 520
53 x 10 = 530
54 x 10 = 540
55 x 10 = 550
56 x 10 = 560
57 x 10 = 570
58 x 10 = 580
59 x 10 = 590
60 x 10 = 600
61 x 10 = 610
62 x 10 = 620
63 x 10 = 630
64 x 10 = 640
65 x 10 = 650
66 x 10 = 660
67 x 10 = 670
68 x 10 = 680
69 x 10 = 690
70 x 10 = 700
71 x 10 = 710
72 x 10 = 720
73 x 10 = 730
74 x 10 = 740
75 x 10 = 750
76 x 10 = 760
77 x 10 = 770
78 x 10 = 780
79 x 10 = 790
80 x 10 = 800
81 x 10 = 810
82 x 10 = 820
83 x 10 = 830
84 x 10 = 840
85 x 10 = 850
86 x 10 = 860
87 x 10 = 870
88 x 10 = 880
89 x 10 = 890
90 x 10 = 900
91 x 10 = 910
92 x 10 = 920
93 x 10 = 930
94 x 10 = 940
95 x 10 = 950
96 x 10 = 960
97 x 10 = 970
98 x 10 = 980
99 x 10 = 990
100 x 10 = 1000

