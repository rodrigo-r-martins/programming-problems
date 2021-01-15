"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

=> Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[5,6]
"""

def findAllDisappearedNumbers(nums):
  nums_set = set(nums)
  complete_set = set(range(1, len(nums)+1))
  return list(complete_set-nums_set)


if __name__ == "__main__":
  nums = [4,3,2,7,8,2,3,1]
  print(findAllDisappearedNumbers(nums))