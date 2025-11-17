
# Given three numbers n
# , k
#  and a
# . Identify whether the data type of n×ka
#  is int, long long or double.

# Input
# Only one line containing three numbers n
# , k
#  and a
#  (1≤a,k,n≤2147483647
# ).

# Output
# Print "int", "long long" or "double" (without quotes) as described in the statement.








n,k,a = map(int,input().split())


if((n*k)%a!=0):
 print("double")
elif (n*k)//a <= 2147483647:
 print("int")
else:
 print("long long") 
 








