d={1:{"name":"frathunan","dept":"cse","year":4},
  2:{"name":"gopi","dept":"b.com","year":3},
  3:{"name":"santhosh","dept":"EEE","year":4}}
a=list(d.keys())
b=int(input("Enter the sudent id:"))
x=input("Enter the key :")
y=input("Enter the value:")
o={x:y}
d[b].update(o)
print(d)


#Reault
Enter the sudent id:1
Enter the key :name
Enter the value:valla
{1: {'name': 'valla', 'dept': 'cse', 'year': 4}, 2: {'name': 'gopi', 'dept': 'b.com', 'year': 3}, 3: {'name': 'santhosh', 'dept': 'EEE', 'year': 4}}
