a = int(input())
b = int(input())
c = int(input())

max_num = a if (a > b and a > c) else (b if b > c else c)

print("max = ",max_num)