

def pyramid(n,i):
 if i==n+1:
  return
 pyramid(n,i+1)
 print(" "*(n-i),end="")
 print("*"*(2*i-1)) 

n=int(input()) 
pyramid(n,1)