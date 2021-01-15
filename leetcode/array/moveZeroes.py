"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

=> Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
  You must do this in-place without making a copy of the array.
  Minimize the total number of operations.
"""

def moveZeroes(nums):
  # Operating with not in-place solution -> O(n)
  # if len(nums) == 0:
  #   return nums
  # result = []
  # index = 0
  # for number in nums:
  #   if number != 0:
  #     result.insert(index, number)
  #     index += 1
  #   else:
  #     result.append(number)
  # return result

  # In-place solution -> O(n)
  position = 0
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[position], nums[i] = nums[i], nums[position]
      position += 1
  return nums

  # O(n^2) solution
  # for i in range(len(nums)-1):
  #   for j in range(i+1, len(nums)):
  #       if nums[i] == 0 and nums[j] != 0:
  #         nums[i], nums[j] = nums[j], nums[i]
  # return nums

if __name__ == "__main__":
  nums = [4,2,4,0,0,3,0,5,1,0]
  print(moveZeroes(nums))