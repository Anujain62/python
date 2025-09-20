# type of string writing
# type - 1
str = 'anu'
# type - 2
str = "anu"
# type - 3
str = """anu"""


# str1 = "this is a string.\n we are creating it in python."
# print(str1)


# operations

# 1) concatenation
# str1 = "apna"
# str2 = "collage"
# finalStr = str1 + str2
# print(finalStr)


# 2) length
# str1 = "apna"
# len1 = len(str1)
# print(len1)
# str2 = "collage"
# len2 = len(str2)
# print(len2)
# finalStr = str1 + " " + str2
# print(len(finalStr))



#3) idexing -> 0 based indexing
# str = "apna_collage"
# ch = str[0]
# print(ch)
# # str[3] = "a"    #this was not allowed



#4) slicing -> accessing parts of a string
# syntax = string_name[starting_idx : ending_idx],including starting index and excluding end index 
# here indexing starts from forward direction and numbering is start from 0
str = "apna collage"
# print(str[5:len(str)])
# print(str[:5])  #it means starting idx is 0
# print(str[5:])   #it means last idx is length of string
# print(str[1:10:2])  #here third number passed as jumping the index by (pass_number - 1)

# here indexing starts from backward direction and numbering is start from -1
# str = "apple"
# print(str[-5:-2])



# 5) functions

# string_name.endswith("sub_string") -> returns true if string ends with sub-string.
# str = "i am studying python from apnacollage"
# print(str.endswith("age"))

# string_name.capitalize() -> capitalizez 1st character
# str = "i am studying python from apnacollage"
# print(str.capitalize())

# string_name.replace(old,new) -> replace all occurrences of old with new
# str = "i am studying python from apnacollage"
# print(str.replace("python","Js"))

# string_name.find(word) -> returns 1st index of 1st occurrence
# str = "i am from studying python from apnacollage"
# print(str.find("from"))

# string_name.count("sub_string") -> counts the occurences of sub-string in string
# str = "i am studying python from apnacollage"
# print(str.count("a"))



