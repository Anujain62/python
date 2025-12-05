# grade students based on marks -> 
# marks >= 90 , grade = A
# 90 > marks >= 80 , grade = B
# 80 > marks >= 70 , grade = C
# 70 > marks , grade = D


marks = int(input("Enter marks :"))
if(marks >= 90):
 print("A")
elif(marks < 90 and marks >= 80):
 print("B") 
elif(marks < 80 and marks >= 70):
 print("C") 
else:
 print("D") 











