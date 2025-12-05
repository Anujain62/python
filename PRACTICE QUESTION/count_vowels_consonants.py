

str = input("enter a string:")
vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

# logic - 1
# for ele in str:
#  if ele in vowels:
#   v_count+=1
#  elif(ele == " "):
#   continue
#  else:
#   c_count+=1



# logic - 2
for ch in str:
 if ch.isalpha():   #it is in-build function, it checks string is character or not
  if ch in vowels:
   v_count+=1
  else:
   c_count+=1 

print("vowel counts = ",v_count)
print("consonant counts = ",c_count)   