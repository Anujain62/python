
n = int(input())
lst  = list(map(int,input().split()))

front = 0
end = n-1
if n%2!=0:
 while front<end:
  print(lst[front],lst[end],end=" ")
  front+=1
  end-=1
 print(lst[front]) 
else:
 while front<=end:
  print(lst[front],lst[end],end=" ")
  front+=1
  end-=1  
