# Given a number N. Print the Fibonacci number of N.

# Note: In order to create the Fibonacci sequence use the following function:

# fib(1) = 0.
# fib(2) = 1.
# fib(n) = fib(n - 1) + fib(n - 2).
# Input
# Only one line containing a number N (1 ≤ N ≤ 50).

# Output
# Print the Fibonacci number of N.



n = int(input())

fibo1=0
fibo2=1
if n==1:
 print(fibo1)
if n==2:
 print(fibo2) 
if n>2:
 for i in range(2,n):
  fibo3 = fibo1+fibo2
  fibo1,fibo2 = fibo2,fibo3
 print(fibo2) 


