
def distinct(lst):
 s=set(lst)
 return len(s)

n = int(input())
if n == 0:         
 print(0)
else:
 lst = list(map(int, input().split()))
 print(distinct(lst))