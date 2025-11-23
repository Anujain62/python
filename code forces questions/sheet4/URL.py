
s = input()
temp=s.split("?")[1]

lst = temp.split("&")
for i in lst:
 key,value = i.split("=")
 print(f"{key}: {value}")



