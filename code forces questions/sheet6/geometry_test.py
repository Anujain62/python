import math
r,s=map(int,input().split())

if (r*2) >= s*math.sqrt(2):
 print("Circle")
elif s>(r*2):
 print("Square") 
else:
 print("Complex") 