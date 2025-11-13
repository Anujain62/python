# Given two person names.

# Each person has {"the first name" + "the second name"}

# Determine whether they are brothers or not.

# Note: The two persons are brothers if they share the same second name.

# Input
# First line will contain two Strings F1, S1 which donates the first and second name of the 1st person.

# Second line will contain two Strings F2, S2 which donates the first and second name of the 2nd person.

# Output
# Print "ARE Brothers" if they are brothers otherwise print "NOT".



person1 = input()
person2 = input()

name1,secName1 = person1.split()
name2,secName2 = person2.split()
if(secName1.lower()==secName2.lower()):
 print("ARE Brothers")
else:
 print("NOT") 