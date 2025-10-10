import random

max_attenpt = 10
attempt = 0
randomNum = random.randint(1,100)

while attempt<max_attenpt:
 num = int(input(f"{attempt} Enter your guess :"))
 attempt+=1
 try:
  if(num==randomNum):
   print("Congrats, you guess right!")
   break
  elif(num<randomNum):
   print("Too Low!")
  else:
   print("Too Hight!") 
 except Exception as e:
  print(e)
else:
 print("Out of attempts!")    

