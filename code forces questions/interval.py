# Given a number X. Determine in which of the following intervals the number X belongs to:

# [0,25], (25,50], (50,75], (75,100]

# Note:

# if X belongs to any of the above intervals print "Interval " followed by the interval.
# if X does not belong to any of the above intervals print "Out of Intervals".
# The symbol '(' represents greater than.
# The symbol ')' represents smaller than.
# The symbol '[' represents greater than or equal.
# The symbol ']' represents smaller than or equal.
# For example:

# [0,25] indicates numbers between 0 and 25.0000, including both.

# (25,50] indicates numbers greater than 25: (25.00001) up to 50.0000000.

# Input
# Only one line containing a number X ( - 1000 ≤ X ≤ 1000).

# Output
# Print the answer to the problem above.







x = float(input())
if(0.0<=x<=25.0):
 print("Interval [0,25]")
elif(25.0<x<=50.0):
 print("Interval (25,50]") 
elif(50.0<x<=75.0):
 print("Interval (50,75]") 
elif(75.0<x<=100.0):
 print("Interval (75,100]") 
else:
 print("Out of Intervals") 