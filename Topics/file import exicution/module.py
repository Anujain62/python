def myFunc():
 print("Hello world!")

myFunc()

#if we runs it is inside the same file so it prints "__main__" and if we runs another file where we import this file so it prints file name where this code is present
# means if we runs module file so it prints "__main__" and if we runs main file so it prints "module"
# print(__name__)       



# this runs only when we runs module.py file, if we runs main.py file so this code does not runs.
if __name__ == "__main__":
 # if this code is directly exicuted by running the file its present in
 print("we are directly running this code")
 print(__name__)