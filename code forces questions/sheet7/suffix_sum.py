
def suffix(arr,left,right):
 if left==right:
  return 0
 return arr[left]+suffix(arr,left+1,right)

n,m =map(int,input().split())
lst=list(map(int,input().split()))
print((suffix(lst,n-m,n)))