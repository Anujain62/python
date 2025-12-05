
def findLcm(x,y):
 return x*y

def findGcd(x,y):
 if(x>y):
  z = y 
 else:
  z = x 
 for i in range(z,0,-1):
  if(x%i==0 and y%i==0):
   return i 
 return -1   

n = int(input("Enter total number of testcases : "))
print("Enter value of x,y : ")
lcmList = []
gcdList = []
for i in range(0,n,1):
 x = input()
 y = input()
 lcm = findLcm(x,y)
 gcd = findGcd(x,y)
 lcmList.append(lcm)
 gcdList.append(gcd)

for i in range(0,len(lcmList),1):
 print(lcmList[i],gcdList[i])