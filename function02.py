#Assign Roll Number 


def add():
    d = {1:{"name":"frathunan","dept":"cse","year":4},
  2:{"name":"gopi","dept":"b.com","year":3},
  3:{"name":"santhosh","dept":"EEE","year":4}}
    v=list(d.keys())
    c=max(v)
    n = c + 1
    a = input("Enter the student Name:")
    b = input("Enter the student dept:")
    c = int(input("Enter the student year:"))
    w={n: {"Name": a, "dept": b, "year": c}}
    d.update(w)
    print(d)

add()
