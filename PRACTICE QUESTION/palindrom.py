# WAP to check if a list contains a palindrome of elements.


list_ele = []
size = int(input("enter size of the list:"))
i = 0 
print("enter elements of the list :")
while i<size:
 list_ele.append(int(input()))
 i+=1
copy_list = list_ele.copy()
copy_list.reverse()
if(list_ele == copy_list):
 print("list is palindrom") 
else:
 print("list is not palindrom") 










