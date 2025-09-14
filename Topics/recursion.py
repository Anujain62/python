# when a function calls itself repeatedly 


# print n to 1 backwards
def show(n):
 if(n==0):
  return
 print(n)
 show(n-1)

n = int(input("enter a number:"))
show(n)


















