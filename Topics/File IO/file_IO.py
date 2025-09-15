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
#    'w'         open for writing, truncatin the file first(overwrite the content of the file)
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

# 2) adds to the file
# f = open("D:\Coding\python\Topics\File IO\demo.txt","a")
# f.write("\nhello, I am anu jain")
# f.close()

# if file does not exist, so it is create the new file and open it for reading or writing
# f = open("sample.txt","w")
# f.write("It is created for writing operation of file I/O")
# f.close()






f = open("D:\Coding\python\Topics\File IO\demo.txt","r+")
f.write("abc def ghi")
print(f.read())
f.close()















