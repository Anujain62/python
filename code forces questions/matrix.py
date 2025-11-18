# Given a number N and a 2D array A of size N * N. Print the absolute difference between the summation of its two diagonals (primary diagonal and secondary diagonal).

# Input
# First line contains a number N (1 ≤ N ≤ 100) described above.

# Each of the next N lines will contain N numbers ( - 100 ≤ Ai ≤ 100).

# Output
# Print the absolute difference between the summation of the matrix main diagonals.




n = int(input())
first = 0
second = 0

for i in range(n):
 row = list(map(int, input().split()))
 first += row[i]
 second += row[n - 1 - i]

print(abs(first - second))


