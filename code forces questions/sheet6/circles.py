import math

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

cx1 = (x1 + x2) / 2
cy1 = (y1 + y2) / 2

cx2 = (x3 + x4) / 2
cy2 = (y3 + y4) / 2

r1 = math.hypot(x1 - x2, y1 - y2) / 2
r2 = math.hypot(x3 - x4, y3 - y4) / 2

d = math.hypot(cx1 - cx2, cy1 - cy2)

if d <= r1 + r2:
 print("YES")
else:
 print("NO")
