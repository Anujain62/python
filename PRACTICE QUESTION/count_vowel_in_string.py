
str = input("Enter a string :")
count = 0
for x in str:
 x = x.lower()
 if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
  count+=1
else:
 print("Number of vowels :",count)  
