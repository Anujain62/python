
# Given a mathematical expression. The expression will be one of the following expressions:

# A + B = C, A - B = C and A * B = C

# where A, B, C are three numbers, S is the sign between A and B, and Q the '=' sign

# Print "Yes" If the expression is Right , Otherwise print the right answer of the expression




expression = input()
temp,c=expression.split("=")
if '+' in temp:
 a,b=temp.split("+")
 if(int(a)+int(b)==int(c)):
  print("Yes")
 else:
  print(int(a)+int(b))
elif '-' in temp:
 a,b=temp.split("-")
 if(int(a)-int(b)==int(c)):
  print("Yes")
 else:
  print(int(a)-int(b))
elif '*' in temp:
 a,b=temp.split("*")
 if(int(a)*int(b)==int(c)):
  print("Yes")
 else:
  print(int(a)*int(b))     