
def shift_zero(lst):
 newArr = []
 count=0
 for i in lst:
  if i==0:
   count+=1
  else:
   newArr.append(i) 

 while count>0:
  newArr.append(0)  
  count-=1
 return newArr 


n=int(input())
lst=list(map(int,input().split()))
print(*(shift_zero(lst)))