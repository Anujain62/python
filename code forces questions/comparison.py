# Given a comparison symbol S between two numbers A and B. Determine whether it is Right or Wrong.
# The comparison is as follows: A < B, A > B, A = B.
# Where A, B are two integer numbers and S refers to the sign between them.



expression = input().strip()

if '>' in expression:
 a,b=expression.split('>')
 if(int(a)>int(b)):
  print("Right")
 else:
  print("Wrong") 
elif '<' in expression:
 a,b=expression.split('<')
 if(int(a)<int(b)):
  print("Right")
 else:
  print("Wrong")
elif '=' in expression:
 a,b=expression.split('=')
 if(int(a)==int(b)):
  print("Right")
 else:
  print("Wrong")   
