d={1:{"name":"frathunan","dept":"cse","year":4},
  2:{"name":"gopi","dept":"b.com","year":3},
  3:{"name":"santhosh","dept":"EEE","year":4}}
b=list(d.keys())
for i in range(len(b)):
    x = int(input("Enter the student id:"))
    if x in b:
        print(d[x])

#Result
Enter the student id:1
{'name': 'frathunan', 'dept': 'cse', 'year': 4}
Enter the student id:2
{'name': 'gopi', 'dept': 'b.com', 'year': 3}
Enter the student id:3
{'name': 'santhosh', 'dept': 'EEE', 'year': 4}
