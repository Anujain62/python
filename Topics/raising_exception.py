
a = int(input("enter first number : "))
b = int(input("enter second number : "))

# we can raised error
if(b==0):
 raise ZeroDivisionError("Hey our program is not meant to divide number by zero")
else:
 print(f"the division a/b is {a/b}") 







