
# n = int(input())
# string = input()

# score = 0
# for i in range(len(string)-1):
#  ch=string[i]
#  if ch=='V':
#   score+=5
#  elif ch=='W':
#   score+=2
#  elif ch=='X':
#   temp=string[:i]
#   if (i+1)<(len(string)-1):
#    temp+=string[i+1:]
#   string=temp
#  elif ch=='Y':
#   temp=string[:i]
#   tempCh = ""
#   if (i+1)<(len(string)-1):
#    tempCh = string[i+1]
#    temp+=string[i+1:]
#   string=temp+tempCh
#  elif ch=="Z":
#   if (i+1)<(len(string)-1):
#    temp=""
#    if string[i+1]=='V':
#     score//=5
#     temp=string[:i]
#     temp+=string[i+1:]
#     string=temp
#    elif string[i+1]=='W':
#     score//=2 
#     temp=string[:i]
#     temp+=string[i+1:]
#     string=temp

# print(score)
    


n = int(input())
s = list(input())   # list so we can modify in O(1)

score = 0
i = 0

while i < len(s):
    ch = s[i]

    # --- V ---
    if ch == 'V':
        score += 5
        i += 1

    # --- W ---
    elif ch == 'W':
        score += 2
        i += 1

    # --- X: Remove next char ---
    elif ch == 'X':
        if i + 1 < len(s):
            s.pop(i + 1)        # delete next element
        i += 1                 # move forward

    # --- Y: Move next char to end ---
    elif ch == 'Y':
        if i + 1 < len(s):
            ch2 = s.pop(i + 1)  # remove next
            s.append(ch2)       # send to end
        i += 1

    # --- Z rule ---
    elif ch == 'Z':
        if i + 1 < len(s):
            next_ch = s[i + 1]

            if next_ch == 'V':
                score //= 5
                s.pop(i + 1)    # remove V
            elif next_ch == 'W':
                score //= 2
                s.pop(i + 1)    # remove W

        i += 1

print(score)



