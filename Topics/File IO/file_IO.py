# python can be used to perform operations on a file.(read and write data)
# type of files ->
# 1) text files -> .txt, .docx, .log etc.
# 2) binary files -> .mp4, .mov, .png, .jpeg etc.

# open, read & close file -> we have to open a file before reading or writing
# eg. -> 
# f = open("fine_name","mode")    #file_bame -> sample.txt,demo.docx     #mode -> r-read mode, w-write mode
# data = f.read()
# f.close()

# character           meaning
#    'r'         open for reading(default)
#    'w'         open for writing, truncating the file first(overwrite the content of the file)
#    'x'         create a new file anf open it for writing
#    'a'         open for writing, appending to the end of the file if it exixts
#    'b'         binary mode 
#    't'         text mode(default) 
#    '+'         open a disk file for uploading(reading and writing)






# # reading to a file
# f = open("D:\Coding\python\Topics\File IO\demo.txt" , "r")

# # read() -> it reads entire file, we can pass arguments for reading number of characters from the starting
# # data = f.read()
# # data = f.read(5)

# # readline() -> reads one line at a time 
# data = f.readline()

# print(data)
# f.close()







# writing to a file
# 1) overwrites the entire file
# f = open("D:\Coding\python\Topics\File IO\demo.txt","w")
# f.write("i want to learn JS tomorrow.")
# f.close()

# 2) adds to the file(add at the end)
# f = open("D:\Coding\python\Topics\File IO\demo.txt","a")
# f.write("\nhello, I am anu jain")
# f.close()

# if file does not exist, so it is create the new file and open it for writing
# f = open("sample.txt","w")
# f.write("It is created for writing operation of file I/O")
# f.close()






# f = open("D:\Coding\python\Topics\File IO\demo.txt","r+")
# # it start reading from the where last pointer is present,it means where writing is stops. it overwrite the content of over file.
# f.write("abc def ghi")
# print(f.read())
# f.close()


# open for reading and writing , it is trancated the file, and overwrite the content
# f = open("D:\Coding\python\Topics\File IO\demo.txt","w+")
# print(f.read())
# f.write("abc")
# f.close()


# it does not read anythink, and is append the content
# f = open("D:\Coding\python\Topics\File IO\demo.txt","a+")
# print(f.read())
# f.write("\thello")
# f.close()







# with syntax ->
# with open("file name","mode") as f:
#  variable_name = f.read()

# here does not compulsary file.close(), because it was close automatically
# with open("D:\Coding\python\Topics\File IO\demo.txt","r") as f:
#  print(f.read())

# with open("D:\Coding\python\Topics\File IO\demo.txt","w") as f:
#  f.write("hello")








# deleting a file -> using the os module.
# module(like a code library) is a file writing by another programmer that generally has a function we can use. 
# import os 
# os.remove(filename)

# import os
# pip.remove("sample.txt")










