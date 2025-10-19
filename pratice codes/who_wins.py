n = int(input("Enter a integer : "))
count = 0
winner = "ramesh"
x = 1
y = 2
while n>count:
 if(winner=="ramesh"):
  count+=x
  x+=1
  winner = "suresh"
 else:
  count+=y
  y+=x*2
  winner = "ramesh"
if(count>n and winner=="ramesh"):
 count = count - (x-1)
 print("Ramesh is winner")
elif(count>n and winner=="suresh"):
 count = count - (y-x*2) 
 print("Suresh is winner")


