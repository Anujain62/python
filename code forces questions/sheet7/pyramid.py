

def pyramid(n,i):
 if i==n+1:
  return
 print(" "*(n-i),end="")
 print("*"*(2*i-1)) 
 pyramid(n,i+1)

n=int(input()) 
pyramid(n,1)