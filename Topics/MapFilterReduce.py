
# map -> map applies a function to all the items/elements in an input_list.
# l = [1,2,3,4,5]
# square = lambda x:x*x    #lambda function/expression
# sqList = map(square,l)     #map function, it return values as a object
# print(list(sqList))





# filter -> filter creates a list of items for which the function returns true.
# l = [1,2,3,4,5]
# def even(n):
#  if(n%2==0):
#   return True
#  return False
# onlyEven = filter(even,l)
# print(list(onlyEven))





# reduce -> reduce applies a rolling computation to sequantial pair of elements.
from functools import reduce
l = [1,2,3,4,5]
def sum(a,b):
 return a+b
print(reduce(sum,l))






