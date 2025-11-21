
s = input()
word = "hello"
idx = 0

for ch in s:
 if ch == word[idx]:
  idx += 1
  if idx == 5:
   break

if idx == 5:
 print("YES")
else:
 print("NO")

