# Hady wants to ride a train. He knows his seat number, but he doesn't know the corresponding row or column number of his seat. However, he knows that each row consists of exactly 4
#  seats. The train seats are numbered from zero as shown in the figure:


# Given the seat number, can you find the corresponding row and column numbers of the seat?

# Input
# Only one line containing id
#  (0≤id≤1018
# ) – the seat number.

# Output
# The row and column numbers of the seat.



# n = int(input())

# row=0
# found = False
# seatNo = 0
# column = 0
# reverse = False
# while True:
#  if(column==4):
#   column=3
#  elif(column<0):
#   column=0 
#  if(column<3):
#   reverse=False
#  else:
#   reverse=True 
#  for i in range(4):
#   if(seatNo==n):
#    print(row,column)
#    found=True
#    break
#   seatNo+=1
#   if reverse:
#    column-=1
#   else:
#    column+=1 
#  row+=1 
#  if found:
#   break 







n = int(input())

row = n // 4
pos = n % 4

if row % 2 == 0:
 column = pos
else:
 column = 3 - pos

print(row, column)
