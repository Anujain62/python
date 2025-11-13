# Given a letter X. If the letter is lowercase print the letter after converting it from lowercase letter to uppercase letter. Otherwise print the letter after converting it from uppercase letter to lowercase letter

# Note : difference between 'a' and 'A' in ASCII is 32 .


x = input()
if('a'<=x<='z'):
 print(x.upper())
elif('A'<=x<='Z'):
 print(x.lower()) 