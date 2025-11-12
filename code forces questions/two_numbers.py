
import math
a,b = map(int,input().split())

x = float(a/b) 

print("floor",a,"/",b,"=",math.floor(x))
print("ceil",a,"/",b,"=",math.ceil(x))
print("round",a,"/",b,"=",round(x))