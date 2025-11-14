
# Given a Number N corresponding to a person's age (in days). Print his age in years, months and days, followed by its respective message "years", "months", "days".

# Note: consider the whole year has 365 days and 30 days per month.

# Input
# Only one line containing a number N (0 ≤ N ≤ 106).

# Output
# Print the output, like the following examples.




n = int(input())
year = n//365
n%=365
month = n//30
n%=30
print(year,"years")
print(month,"months")
print(n,"days")

