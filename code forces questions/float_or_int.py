
n = input()

x,y=n.split('.')
if(int(x)!=0 and int(y)!=0):
 print(f"float {x} 0.{y}")
elif(int(x)!=0 and int(y)==0):
 print(f"int {x}") 