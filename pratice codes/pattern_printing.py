n = int(input("Enter number of line :"))



# #1) ****
# #   ***
# #   **
# #   *

# for i in range(0,n,1):
#  for j in range(i,n,1):
#   print("*",end=" ")
#  print() 





# # 2) ****
# #     ***
# #      **
# #       *
# for i in range(0,n,1):
#  for j in range(0,i,1):
#   print(" ",end="")
#  for j in range(0,n-i,1):
#   print("*",end="")
#  print()  






# 3) *
#    **
#    ***
#    ****
for i in range(0,n,1):
 for j in range(0,i+1,1):
  print("*",end="")
 print() 


