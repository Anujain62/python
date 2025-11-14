
# One day, Ali Baba had an easy puzzle that he couldn't solve. The puzzle consisted of 4
#  numbers and his task was to check whether he could get the fourth number using arithmetic operators (+,−,×
# ) between the other three numbers; so that each operator is used only once.

# a□b□c=d
# Can you solve this tricky puzzle for him?
# Input
# Only one line containing four numbers a
# , b
# , c
#  and d
#  (−109≤a,b,c≤109
# ),(−1018≤d≤1018
# ).

# Output
# Print "YES" (without quotes) if you get the fourth number using arithmetic operators, otherwise, print "NO" (without quotes).




# a,b,c,d = map(int,input().split())

# if(a + b + c == d or
#     a + b - c == d or
#     a + b * c == d or
#     a - b + c == d or
#     a - b - c == d or
#     a - b * c == d or
#     a * b + c == d or
#     a * b - c == d or
#     a * b * c == d):
#  print("YES")
# else:
#  print("NO") 








# def apply(x, op, y):
#     if op == '+': return x + y
#     if op == '-': return x - y
#     if op == '*': return x * y

# a, b, c, d = map(int, input().split())

# ops = ['+', '-', '*']

# for op1 in ops:
#     for op2 in ops:

#         # Case 1: (a op1 b) op2 c
#         if apply(apply(a, op1, b), op2, c) == d:
#             print("YES")
#             exit()

#         # Case 2: a op1 (b op2 c)
#         if apply(a, op1, apply(b, op2, c)) == d:
#             print("YES")
#             exit()

# print("NO")









def apply(x, op, y):
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y

def check(a, b, c, d):
    ops = ['+', '-', '*']
    for op1 in ops:
        for op2 in ops:
            # Case 1: (a op1 b) op2 c
            if apply(apply(a, op1, b), op2, c) == d:
                return True
            # Case 2: a op1 (b op2 c)
            if apply(a, op1, apply(b, op2, c)) == d:
                return True
            # Case 3: (a op1 c) op2 b
            if apply(apply(a, op1, c), op2, b) == d:
                return True
            # Case 4: a op1 (c op2 b)
            if apply(a, op1, apply(c, op2, b)) == d:
                return True
            # Case 5: (b op1 c) op2 a
            if apply(apply(b, op1, c), op2, a) == d:
                return True
            # Case 6: b op1 (c op2 a)
            if apply(b, op1, apply(c, op2, a)) == d:
                return True
    return False

a, b, c, d = map(int, input().split())
if check(a, b, c, d):
    print("YES")
else:
    print("NO")