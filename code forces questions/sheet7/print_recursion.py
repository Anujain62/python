

def recursion(n):
 if n<1:
  return
 recursion(n-1)
 print("I love Recursion")

n=int(input())
recursion(n)
