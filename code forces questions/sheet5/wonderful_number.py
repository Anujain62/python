
def odd(n):
 if n%2==0:
  return False
 else:
  return True

def palindrome(n):
 ans="" 
 while n>0:
  temp=n%2
  n//=2
  ans+=str(temp)

 temp="".join(reversed(ans))
 if ans==temp:
  return True
 else:
  return False

n=int(input())  

if odd(n):
 if palindrome(n):
  print("YES")
 else:
  print("NO") 
else:
 print("NO")  


