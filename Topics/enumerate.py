l = [3,523,45,535]


# normal way for printing list
# index = 0
# for item in l:
#  print(f"the iem number at index {index} is {item}")
#  index+=1






# this can be simplified using enumerate function
for index, item in enumerate(l):
 print(f"the iem number at index {index} is {item}")


