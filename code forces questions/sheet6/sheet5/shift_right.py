
def shift(arr,n,x):
 remain=x%n
 for i in range(remain):
  temp = arr[n-1]
  for j in range(n-1,0,-1):
   arr[j]=arr[j-1]
  arr[0]=temp 
 return arr 


n,x=map(int,input().split())
arr=list(map(int,input().split()))
print(*(shift(arr,n,x)))


