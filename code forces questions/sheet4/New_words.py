
# t=input()
# s = t.lower()

# word="egypt"
# i=0
# count=0
# while i<len(s):
#  ans=""
#  if s[i]!="e":
#   i+=1
#   continue
#  for j in range(i,len(s)):
#   if (s[j]=='e' or s[j]=='g' or s[j]=='y' or s[j]=='p' or s[j]=='t') and s[j] not in ans:
#    ans+=s[j]
#  i+=1  
 
#  if ans==word:
#   count+=1  

# print(count)







s = input().lower()

freq = {
    'e': 0,
    'g': 0,
    'y': 0,
    'p': 0,
    't': 0
}

# Count required characters
for ch in s:
    if ch in freq:
        freq[ch] += 1

# Find minimum count (that decides how many times "egypt" can be formed)
print(min(freq.values()))

