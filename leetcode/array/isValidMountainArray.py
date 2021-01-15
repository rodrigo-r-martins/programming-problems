"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:
  arr.length >= 3
  There exists some i with 0 < i < arr.length - 1 such that:
      arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
      arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

=> Example 1:
Input: arr = [2,1]
Output: false

=> Example 2:
Input: arr = [3,5,5]
Output: false

=> Example 3:
Input: arr = [0,3,2,1]
Output: true

=== Constraints ===
  1 <= arr.length <= 104
  0 <= arr[i] <= 104
"""

def isValidMountainArray(arr):
  max_num_pos = arr.index(max(arr))
  if len(arr) < 3:
    return False
  if max_num_pos == 0 or max_num_pos == len(arr)-1:
    return False

  res = False
  i = 0
  while i < max_num_pos:
    if arr[i] < arr[i+1]:
      res = True
    else:
      return False
    i += 1

  i = len(arr)-1
  while i > max_num_pos:
    if arr[i] < arr[i-1]:
      res = True
    else:
      return False
    i -= 1
  return res

if __name__ == "__main__":
  arr = [0,1,2,1,2]
  print(isValidMountainArray(arr))