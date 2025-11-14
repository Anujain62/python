
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

ans = (n*k)//a
INT_MAX = 2**31 - 1
LLONG_MAX = 2**63 - 1

if(ans<=INT_MAX):
 print("int")
elif(ans<=LLONG_MAX):
 print("long long") 
else:
 print("double") 







