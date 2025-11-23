
s = input().split()

for word in s:
 temp=""
 for i in range(len(word)-1,-1,-1):
  temp+=word[i]
 if word==s[len(s)-1]:
  print(temp) 
 else: 
  print(temp,end=" ") 

