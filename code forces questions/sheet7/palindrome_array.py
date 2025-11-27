def palindrome(arr,left,right):
 if left>right:
  return
 
 palindrome(arr,left+1,right-1)
 if arr[left]!=arr[right]:
  return False
 return True

n=int(input())
lst=list(map(int,input().split()))
if palindrome(lst,0,n-1):
 print("YES")
else:
 print("NO") 
