
myList = [1,2,9,5,3,5]



# normal way for printing square of every element of the list
# squaredList = []
# for item in myList:
#  squaredList.append(item*item)
# print(squaredList) 





# using list list comprehensions
squaredList = [i*i for i in  myList]
print(squaredList) 
