# Given two numbers N and M, a 2D array A of size N * M which contains 'x' or '.' only and two numbers X, Y which donates a cell position in A such that X is the row number and Y is the column number.

# Determine whether all neighbors of the given cell are 'x' or not.

# Note: The neighbor cell is any cell that shares an edge or a corner and it should be inside 2D array.

# Input
# First line contains two numbers N, M (2≤N,M≤100) N donates number of rows and M donates number of columns.

# Each of the next N lines will contain M symbol can be ('.' or 'x').

# Last line contains two numbers X, Y (1≤X≤N,1≤Y≤M).

# Output
# Print "yes" if all neighbors of the given cell are 'x' otherwise, print "no" without quotations.



n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
x, y = map(int, input().split())

# Convert to 0-based indexing
x -= 1
y -= 1

# Directions for 8 neighbors
dirs = [(-1,-1), (-1,0), (-1,1),
        (0,-1),    (0,1),
        (1,-1), (1,0),  (1,1)]

ok = True

for dx, dy in dirs:
 nx = x + dx
 ny = y + dy

    # Check if inside grid
 if 0 <= nx < n and 0 <= ny < m:
  if grid[nx][ny] != 'x':
   ok = False
   break

print("yes" if ok else "no")

 