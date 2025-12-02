
def newArray(a,b):
 arr = []
 for i in b:
  arr.append(i)
 for i in a:
  arr.append(i)
 return arr 



n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(*(newArray(a,b)))