"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

=> Example 1:
Input: nums = [2,2,1]
Output: 1

=> Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

=> Example 3:
Input: nums = [1]
Output: 1

=== Constraints ===
  1 <= nums.length <= 3 * 104
  -3 * 104 <= nums[i] <= 3 * 104
  Each element in the array appears twice except for one element which appears only once.
"""

def getSingleNumber(nums):
  nums_dict = {}
  for num in nums:
    if num not in nums_dict.keys():
      nums_dict[num] = 1
    else:
      nums_dict[num] += 1
  for key in nums_dict.keys(): 
    if nums_dict[key] == 1:
      return key
  

if __name__ == "__main__":
  nums = [2,2,1]
  print(getSingleNumber(nums))

  nums = [4,1,2,1,2]
  print(getSingleNumber(nums))

  nums = [1]
  print(getSingleNumber(nums))