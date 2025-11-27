
def print_digits(n):
 if n < 10:       
  print(n, end=" ")
  return
    
 print_digits(n // 10)
 print(n % 10, end=" ")


n=int(input())
for i in range(n):
 x=int(input())
 print_digits(x)
 print()

