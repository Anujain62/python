
def left_max(arr, i, current_max):
 if i == len(arr):
  return

 current_max = max(current_max, arr[i])
 print(current_max, end=" ")
 left_max(arr, i + 1, current_max)


n = int(input())
arr = list(map(int, input().split()))

left_max(arr, 0, float('-inf'))
