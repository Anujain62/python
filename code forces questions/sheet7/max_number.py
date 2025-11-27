def max_num(arr,i):
 if i==len(arr)-1:
  return arr[i]
 
 remain = max_num(arr,i+1)
 return max(remain,arr[i])

n=int(input()) 
lst=list(map(int,input().split()))
print(max_num(lst,0))