
# n,q = map(int,input().split())

# string = input()
# for i in range(q):
#  lst = input().split()
#  if lst[0]=="pop_back":
#   temp=string[:len(string)-1]
#   string=temp
#  elif lst[0]=="front":
#   print(string[0])
#  elif lst[0]=="back":
#   print(string[-1])  
#  elif lst[0]=="reverse":
#   temp = string[:int(lst[1])-1]+string[int(lst[1])-1:int(lst[2])][::-1]+string[int(lst[2]):]
#   string=temp
#  elif lst[0]=="sort":
#   string = list(string)
#   l = int(lst[1]) - 1
#   r = int(lst[2]) - 1
#   string[l:r+1] = sorted(string[l:r+1])
#   string="".join(string[0:len(string)])
#  elif lst[0]=="print":
#   print(string[int(lst[1])-1])
#  elif lst[0]=="substr":
#   temp=string[int(lst[1])-1:int(lst[2])]
#   print(temp)
#  elif lst[0]=="push_back":
#   string=list(string)
#   string.append(lst[1])
#   string = "".join(string[0:len(string)])








n, q = map(int, input().split())
string = input()

for _ in range(q):
 lst = input().split()

 if lst[0] == "pop_back":
  string = string[:-1]

 elif lst[0] == "front":
  print(string[0])

 elif lst[0] == "back":
  print(string[-1])

 elif lst[0] == "reverse":
  l = int(lst[1]) - 1
  r = int(lst[2])
  string = string[:l] + string[l:r][::-1] + string[r:]

 elif lst[0] == "sort":
  l = int(lst[1]) - 1
  r = int(lst[2]) - 1
  s_list = list(string)
  s_list[l:r+1] = sorted(s_list[l:r+1])
  string = "".join(s_list)

 elif lst[0] == "print":
  print(string[int(lst[1]) - 1])

 elif lst[0] == "substr":
  l = int(lst[1]) - 1
  r = int(lst[2])
  print(string[l:r])

 elif lst[0] == "push_back":
  string += lst[1]





