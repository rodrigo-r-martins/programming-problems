"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

=> Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

=> Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

=> Example 3:
Input: digits = [0]
Output: [1]

=== Constraints ===
  1 <= digits.length <= 100
  0 <= digits[i] <= 9
"""

def plusOne(digits):
  number = "".join(map(str, digits))
  zeros_at_beginning = -1
  is_zero = True
  i = 0
  while is_zero and i < len(digits):
    if number[i] == "0" and len(number) > 1:
      zeros_at_beginning += 1
    else:
      is_zero = False
    i += 1
  if zeros_at_beginning >= 1:
    number = "0"*zeros_at_beginning + str(int(number)+1)
  else:
    number = str(int(number)+1)
  number = list(number)
  return number


if __name__ == "__main__":
  digits = [1,2,3]
  print(plusOne(digits))

  digits = [4,3,2,1]
  print(plusOne(digits))
  
  digits = [0, 0]
  print(plusOne(digits))
  