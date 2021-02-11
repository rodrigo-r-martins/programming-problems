"""
Given two strings s and t , write a function to determine if t is an anagram of s.

=> Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

=> Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

def isValidAnagram(s, t):
  # if len(s) != len(t):
  #   return False
  # for letter in s:
  #   if letter not in t or s.count(letter) != t.count(letter):
  #     return False
  # return True

  if len(s) != len(t):
    return False
  sLetters = {}
  tLetters = {}
  for letter in s:
    if letter in sLetters:
      sLetters[letter] += 1
    else:
      sLetters[letter] = 1
  for letter in t:
    if letter in tLetters:
      tLetters[letter] += 1
    else:
      tLetters[letter] = 1
  for letter in sLetters:
    if letter not in tLetters or sLetters[letter] != tLetters[letter]:
      return False
  return True  


if __name__ == "__main__":
  s = "anagram"
  t = "nagaram"
  print(isValidAnagram(s, t))

  s = "rat"
  t = "car"
  print(isValidAnagram(s, t))