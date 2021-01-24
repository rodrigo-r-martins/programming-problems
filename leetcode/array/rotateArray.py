"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:
  Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
  Could you do it in-place with O(1) extra space?

=> Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

=> Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

=== Constraints ===
  1 <= nums.length <= 2 * 104
  -231 <= nums[i] <= 231 - 1
  0 <= k <= 105
"""

def rotateArray(nums, k):
  for i in range(k):
    num = nums.pop()
    nums.insert(0, num)
  return nums

  # nums_to_extend = nums[:k]
  # nums_to_start = nums[len(nums)-k:]
  # if len(nums) % k == 0:
  #   nums = nums_to_start + nums_to_extend
  # else:
  #   nums = nums[k:k+1]
  #   nums = nums_to_start + nums + nums_to_extend
  # return nums

  #nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
  return nums



if __name__ == "__main__":
  nums = [1,2,3,4,5,6,7]
  k = 3
  print(rotateArray(nums, k))

  nums = [-1,-100,3,99]
  k = 2
  print(rotateArray(nums, k))