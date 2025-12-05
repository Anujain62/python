#1) create a new file "practice.txt" using python.add the follwing data in it:
# Hi everyone 
# we are learning file I/O
# using Java.
# I like programming in Java.

f = open("practice.txt","w+")
f.write("Hi everyone \nwe are learning file I/O \nusing Java. \nI like programming in Java.")
f.close()



# 2) write a file replaces all occurrences of "Java" with "python" in above file.
# f = open("practice.txt","r")
# data = f.read()
# # it was returns new data after modification
# new_data = data.replace("Java","python")
# print(new_data)

# f = open("practice.txt","w")
# f.write(new_data)
# f.close()



# 3) search if the word "learing" exists in the file or not.
# f = open("practice.txt","r")
# data = f.read()
# if(data.find("learn") != -1):
#  print("found")
# else:
#  print("not found") 
# f.close() 




# 4) write a file in which line of the file does the word "learning" occur first.
# print -1 if word not found
# f = open("practice.txt","r")
# word = "Java"
# data = True
# is_present = False
# line_no = 1
# while data:
#  data = f.readline()
#  if(word in data):
#   print(line_no)
#   is_present = True
#   break
#  line_no+=1 
# if(not data):
#  print("-1")
# f.close()




# 5) from a file containing numbers by comma, print the count of even numbers.
f = open("practice.txt","w")
f.write("1, 2, 4, 5, 6, 7, 8, 9, 12, 14, 23, 18, 34, 0")
f.close() 

f = open("practice.txt","r")
data = f.read()
count = 0

# manual method
# num = ""
# for i in range(len(data)):
#  if(data[i]==","):
#   temp = int(num)
#   if(temp%2 == 0):
#    count+=1
#    num = ""
#   else:
#    num = "" 
#  else:
#   num += data[i] 
# print("number of even numbers :",count) 


# spliting method
# nums = data.split(",")
# for val in nums:
#  temp = int(val)
#  if(temp%2 == 0):
#   count+=1
# print(count)  






