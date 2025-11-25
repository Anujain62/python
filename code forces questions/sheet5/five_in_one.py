
def get_max(arr):
 return max(arr)

def get_min(arr):
 return min(arr)

def is_prime(x):
 if x <= 1:
  return False
 for i in range(2, int(x**0.5) + 1):
  if x % i == 0:
   return False
 return True

def count_primes(arr):
 return sum(1 for x in arr if is_prime(x))

def is_palindrome(x):
 return str(x) == str(x)[0: : -1]

def count_palindromes(arr):
 return sum(1 for x in arr if is_palindrome(x))

def count_divisors(x):
 cnt = 0
 for i in range(1, int(x**0.5) + 1):
  if x % i ==0:
   cnt += 1
   if i != x // i:
    cnt += 1
 return cnt

def max_divisors_number(arr):
 best_num = arr[0]
 best_div = count_divisors(arr[0])

 for x in arr:
  d = count_divisors(x)
  if d > best_div or (d == best_div and x > best_num):
   best_div = d
   best_num = x

 return best_num

n = int(input())
arr = list(map(int, input().split()))

print("The maximum number :", get_max(arr))
print("The minimum number :", get_min(arr))
print("The number of prime numbers :", count_primes(arr))
print("The number of palindrome numbers :", count_palindromes(arr))
print("The number that has the maximum number of divisors :", max_divisors_number(arr))
