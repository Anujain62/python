
# nums = [7,8,9,4,2]
# it = iter(nums)
# print(it.__next__())
# print(it.__next__()) 
# print(next(it))



# iter() method - it gives object of the iterator.
# next() method - which is gives next value/object

class TopTen:
 def __init__(self):
  self.num = 1
 def __iter__(self):
  return self 
 def __next__(self):
  if(self.num<=10):
   val = self.num 
   self.num += 1
   return val 
  else:
   raise StopIteration

values = TopTen()
for i in values:
 print(i) 


