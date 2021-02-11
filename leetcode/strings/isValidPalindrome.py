"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false

=== Constraints ===
  s consists only of printable ASCII characters.
"""

def isValidPalindrome(s):
  letters = []
  for letter in s:
    if letter.isalpha() or letter.isnumeric():
      letters.append(letter)
  s = "".join(letters).lower()
  return s == s[::-1]

if __name__ == "__main__":
  s = "A man, a plan, a canal: Panama"
  print(isValidPalindrome(s))

  s = "race a car"
  print(isValidPalindrome(s))