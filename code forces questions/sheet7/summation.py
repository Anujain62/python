

def summation(arr,i):
 if len(arr) == i:
  return 0
 return arr[i] + summation(arr,i+1)

n=int(input()) 
lst=list(map(int,input().split()))
print(summation(lst,0))