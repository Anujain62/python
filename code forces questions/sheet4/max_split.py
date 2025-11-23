
# s = input()
# i = 0
# ans = []
# count=0
# while i<len(s):
#  temp = ""
#  while i<len(s) and s[i]!='R':
#   temp+=s[i]
#   i+=1
#  while i<len(s) and s[i]!='L':
#   temp+=s[i]
#   i+=1
#  count+=1
#  ans.append(temp)

# print(count)
# for x in ans:
#  print(x)













s = input()
balance = 0
ans = []
temp = ""

for ch in s:
    temp += ch
    if ch == 'L':
        balance += 1
    else:
        balance -= 1
    
    if balance == 0:   # Found a balanced substring
        ans.append(temp)
        temp = ""

print(len(ans))
for x in ans:
    print(x)
