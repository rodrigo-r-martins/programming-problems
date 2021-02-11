"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

=> Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

=> Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

=== Constraints ===
  0 <= strs.length <= 200
  0 <= strs[i].length <= 200
  strs[i] consists of only lower-case English letters.
"""

def longestCommonPrefix(strs):
  if not strs or len(strs) < 2:
    return ""
  if not strs[0]:
    return ""
  if len(strs) < 2:
    return strs[0]

  i = 0
  prefix = ""
  while i < len(strs[0]):
    prefix = strs[0][:i+1]
    j = 1
    is_common = True
    while j < len(strs) and is_common:
      prefix_strs_j = strs[j][:i+1]
      if prefix_strs_j != prefix:
        is_common = False
      j += 1
    if not is_common:
      return prefix[:-1]
    i += 1
  return prefix
  

      
if __name__ == "__main__":
  strs = ["flower","flow","flight"]
  print(longestCommonPrefix(strs))

  strs = ["dog","racecar","car"]
  print(longestCommonPrefix(strs))

  strs = ["flower","flower","flower", "flower"]
  print(longestCommonPrefix(strs))

