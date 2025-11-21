
s=input()
total=0
idx = 0
ans=[]
temp = set(s)
# sorted(temp)
while total<len(s):
 x=sorted(temp)[idx]
 idx+=1
 if x not in ans:
  ans.append(x)
  print(x,":",s.count(x))
  total+=s.count(x)  



