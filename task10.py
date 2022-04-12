class math:
    def func_msg(self):
        x = int(input("Enter the First value:"))
        y = int(input("Enter the second value:"))
        z = input("Enter your char:")
        if "+" == z:
            print("add",x+y)
        elif "-" == z:
            print("sub",x-y)
        elif "*" == z:
            print("multiple",x*y)
        else:
            print("No such charcter")
opj=math()
opj.func_msg()


#Result
Enter the First value:10
Enter the second value:10
Enter your char:+
add 20
