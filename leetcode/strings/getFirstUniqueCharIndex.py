"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.


=> Examples:
s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

Note: You may assume the string contains only lowercase English letters.
"""

def getFirstUniqueCharIndex(string):
  # for i, letter in enumerate(string):
  #   if string.count(letter) == 1:
  #     return i
  # return -1

  letters = {}
  for letter in string:
    if letter in letters:
      letters[letter] += 1
    else:
      letters[letter] = 1
  for i, letter in enumerate(string):
    if letters[letter] == 1:
      return i
  return -1


if __name__ == "__main__":
  string = "leetcode"
  print(getFirstUniqueCharIndex(string))

  string = "loveleetcode"
  print(getFirstUniqueCharIndex(string))