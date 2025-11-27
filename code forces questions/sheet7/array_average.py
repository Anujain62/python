
def average(arr, i, n):
 if i == n:
  return 0
 return arr[i] + average(arr, i + 1, n)

n = int(input())
lst = list(map(int, input().split()))

avg = average(lst, 0, n) / n
print(f"{avg:.6f}")


