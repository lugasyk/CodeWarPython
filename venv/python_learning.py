def longest_consec(strarr, k):
        # your code
    n = len(starr)
    if n == 0 or k > n or k <= 0:
        return ""

    longest = index = 0
    for i in range(n - k + 1):
        length = sum([len(s) for s in strarr[i: i + k]])
        if length > longest:
            longest = length
            index = i

        return ''.join(strarr[index: index + k])

# find_uniq
def find_uniq(arr):
    # your code here
  arr.sort()
  if arr[0] < arr[1]:
      n = arr[0]
  elif arr[-1] > arr[-2]:
        n = arr[-1]
  return n

# or
def find_uniq(arr):
    if arr.count(max(arr)) > 1: # your code here
        return min(arr)
    else:
        return max(arr)