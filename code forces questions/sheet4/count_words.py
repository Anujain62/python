
s = input().split(" ")
count=0
for i in s:
 if i[0].isalpha():
  count+=1

print(str(count))