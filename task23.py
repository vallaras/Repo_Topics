def math(x):
	sum=0
	for i in range(0,x+1):
		sum=sum+i*i*i
	return sum
x=int(input("Enter the value:"))

print(math(x))

#result
Enter the value:5
225
