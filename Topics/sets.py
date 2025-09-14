# set is the collection of the unordered items and set is mutable.
# each element in the set must be unique & immutable.
# here we only stored immutable type elements like tuple.
# enpty set syntax -> num = set()
# eg. ->
# nums = {1,2,2,2,3}
# repeated elements stored only once, so it resolved to {1,2,3}


# empty set syntax
# collection = set()
# print(type(collection))
# print(collection)

# collection = {1,2,3,4,2,2,"hello","anu"}
# print(type(collection))
# print(collection)



# methods
collection = set()

# add an element
collection.add(1)
collection.add(2)
collection.add(3)
collection.add("anu")
collection.add((1,2,3))
collection.add(1)
print(collection)

# remove an element
# collection.remove(1)
# print(collection)

# empties the set
# collection.clear()
# print(collection)

# remove the random value
# print(collection.pop())
# print(collection.pop())

# combines both set values and returns new
# set2 = (10,20,30)
# print(collection.union(set2))

# combines common values and returns new
set2 = (1,2,3)
print(collection.intersection(set2))


