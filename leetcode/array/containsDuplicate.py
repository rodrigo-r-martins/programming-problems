"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

=> Example 1:
Input: [1,2,3,1]
Output: true

=> Example 2:
Input: [1,2,3,4]
Output: false

=> Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def containsDuplicate(nums):
  res = {}
  for num in nums:
    if num not in res.keys():
      res[num] = 1
    else:
      return True
  return False

  # res = { num:0 for num in nums }
  # for num in nums:
  #   res[num] += 1
  #   if res[num] > 1:
  #     return True
  # return False


if __name__ == "__main__":
  nums = [1,1,1,3,3,4,3,2,4,2]
  print(containsDuplicate(nums))

  nums = [1,2,3,4]
  print(containsDuplicate(nums))

  nums = [1,2,3,1]
  print(containsDuplicate(nums))