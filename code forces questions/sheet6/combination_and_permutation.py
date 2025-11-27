
def fact(n):
 if n<=1:
  return 1
 return n*fact(n-1)
a,b=map(int,input().split())
NCR = fact(a)/(fact(b)*fact(a-b))
NPR = fact(a)/fact(a-b)

print(int(NCR),int(NPR))