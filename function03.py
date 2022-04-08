#List of Dict
def check():
  d = {1: {"name": "frathunan", "dept": "cse", "year": 4},
       2: {"name": "gopi", "dept": "b.com", "year": 3},
       3: {"name": "santhosh", "dept": "EEE", "year": 4}}
  b = list(d.keys())
  x = int(input("Enter the stud_id:"))
  if x in b:
    for key, value in d[x].items():
      print(key, ":", value)

check()


#SEARCH Dict

def search():
  d = {1: {"name": "frathunan", "dept": "cse", "year": 4},
       2: {"name": "gopi", "dept": "b.com", "year": 3},
       3: {"name": "santhosh", "dept": "EEE", "year": 4}}
  b=list(d)
  x=int(input("Enter the student id:"))
  if x in b:
    print(d[x])
search()

