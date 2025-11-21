
s = input()
result = ""
for i in s:
 if i==',':
  result+=" "
 elif i.islower():
   result+=i.upper()
 elif i.isupper():
  result+=i.lower()
 else:
  result+=i 

print(result)


