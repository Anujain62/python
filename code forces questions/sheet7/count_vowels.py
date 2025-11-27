
def vowels(s,i):
 if i==len(s):
  return 0
 if s[i] in 'aeiou':
  return 1+vowels(s,i+1)
 else: 
  return vowels(s,i+1) 



s=input().lower()
print(vowels(s,0))

