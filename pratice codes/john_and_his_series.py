
a = int(input("Enter first term :"))
d = int(input("Enter common difference :"))
n = int(input("term number:"))

nth_term = a + (n-1)*d 

summation = n/2*(a+nth_term)

print("nth term :",nth_term)
print("Sum of n terms :",summation)