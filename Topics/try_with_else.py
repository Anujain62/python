try:
 a = int(input("hey, enter a number :"))
 print(a)

except Exception as e:
 print(e) 

else:       #it exicutes when try was exicutes successfully, if any exception accors so else does not exicutes.
 print("I am inside else")
