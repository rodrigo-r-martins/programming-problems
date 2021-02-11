"""
Given two arrays, write a function to compute their intersection.

=> Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

=> Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
  Each element in the result should appear as many times as it shows in both arrays.
  The result can be in any order.

Follow up:
  What if the given array is already sorted? How would you optimize your algorithm?
  What if nums1's size is small compared to nums2's size? Which algorithm is better?
  What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

def getIntersection(nums1, nums2):
  intersect = []
  for num in nums1:
    if num in nums2:
      intersect.append(num)
      nums2.remove(num)
  return intersect

  # intersect = []
  # nums_dict = {}
  # smaller = nums1 if len(nums1) <= len(nums2) else nums2
  # larger = nums1 if len(nums1) > len(nums2) else nums2
  # for num in smaller:
  #   if num in nums_dict:
  #     nums_dict[num] += 1
  #   else:
  #     nums_dict[num] = 1
  # for num in larger:
  #   if num in nums_dict and nums_dict[num] != 0:
  #     intersect.append(num)
  #     nums_dict[num] -= 1
  # return intersect


if __name__ == "__main__":
  nums1 = [1,2,2,1]
  nums2 = [2,2]
  print(getIntersection(nums1, nums2))

  nums1 = [4,9,5]
  nums2 = [9,4,9,8,4]
  print(getIntersection(nums1, nums2))
