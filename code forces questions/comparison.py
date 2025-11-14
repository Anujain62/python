
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
