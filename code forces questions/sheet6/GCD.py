
import math

A, B = map(int, input().split())

g = math.gcd(A, B)
l = A // g * B   

print(g, l)

