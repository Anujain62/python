# dictionaries are used to store data values in "key":value pairs.
# they  are unordered, mutable(changesable) & don't allow duplicate keys.
# here we can stores lists or tuples inside the value.
# eg. -> creation of dictionary 
# dict = {
#  "name" : "anu",
#  "CGPA" : 7.8,
#  "marks" : [85,90,87]
# }



# empty dictionary -> 
# s = {}



# single dictionary ->
# info = {
#  "key" : "value",
#  "name" : "anu",
#  "subjects" : ["python","c","java"],
#  "topics" : ("dic", "sets"),
#  "age" : 20,
# }
# print(type(info))
# print(info)

# here we used key name for accessing specific value,becuase here indexing does not works.
# print(info["name"])
# print(info["topics"])

# here we can re-assign values through the key name
# info["age"] = 25
# print(info)

# we can add new key : value pair
# info["surname"] = "jain"
# print(info)





# nested dictionaries

# student = {
#  "name" : "anu jain",
#  "subjects" : {
#   "phy" : 97,
#   "chem" : 98,
#   "math" : 95
#  }
# }
# print(student)
# print(student["subjects"]["chem"])






# methods
# info = {
#  "key" : "value",
#  "name" : "anu",
#  "subjects" : ["python","c","java"],
#  "topics" : ("dic", "sets"),
#  "age" : 20,
# }
# print(info)

# returns all keys
# print(info.keys())

# returns all values
# print(info.values())

# returns all (key,value) pairs as tuple
# print(info.items())

# returns the value according to key,it returns none if key is not present in the dictionary and continue the exicution of below code,where if we use [key] based access and here key is not present in the dictionary,so it gives error and then does not exicute the below code, so we use get() funtion in maximum times  
# print(info.get("name2"))
# returns an error
# print(info["name2"])

# inserts the specified items to the dictionary
# 1)
# info.update({"city": "jabalpur"})
# print(info)

# 2) if we add same key name so this is overrite the value of previous key, this does not create the duplicate key
# new_dict = {"city":"jabalpur", "branch":"CSE"}
# info.update(new_dict)
# print(info)








# how to marge keys and values
keys = ['navin','kiran','harsh']
values = ['python','java','js']
data = dict(zip(keys,values))      #this is marge keys and values in one dictionary.
print(data)









