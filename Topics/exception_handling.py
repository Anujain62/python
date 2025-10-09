# types of errors -> compile time, logical, run time.
# 1) compile time error -> syntactical errors -> 
# eg. -> missing (:), wrong spelling

# 2) logical error -> 
# eg. -> 2+3 = 5

# 3) run time error -> divided by zero
# eg. -> 6/0 -> it gives error


# statement is divides into two parts -> 
# 1) normal part -> will  not give any error 
# 2) critical 




a = int(input("enter first number : "))
b = int(input("enter second number :"))
try:
 print("Resource open")
 print(a/b)
except Exception as e:
 print("Error : ",e) 
#finally block will be executed if we get error as well as if we don't get the error. 
finally:
 print("Resource closed")









