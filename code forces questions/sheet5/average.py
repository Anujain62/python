

def average(arr,n):
 s=0
 s = sum(arr)
 ave = s/n 
 return ave



n=int(input())
arr=list(map(float,input().split()))
print(f"{(average(arr,n)):.6f}")
