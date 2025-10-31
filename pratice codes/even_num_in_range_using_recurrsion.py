
def evenNum(x,n):
 if(x>n):
  return
 elif(x%2==0):
  print(x)
 evenNum(x+1,n)


n=int(input("Enter a number :"))
evenNum(1,n)