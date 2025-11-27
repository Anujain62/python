
def even_index(arr,n):
 if n<0:
  return
 
 if n%2==0:
  print(arr[n],end=" ")
 even_index(arr,n-1) 

n=int(input())
lst = list(map(int,input().split()))
even_index(lst,n-1)