"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

=> Example 1:
Input: x = 123
Output: 321

=> Example 2:
Input: x = -123
Output: -321

=> Example 3:
Input: x = 120
Output: 21

=> Example 4:
Input: x = 0
Output: 0

=== Constraints ===
  -231 <= x <= 231 - 1
"""

def reverseInteger(integer):
  maximum = 2 ** 31
  minimum = (2 ** 31) * -1
  integer = "-" + str(integer)[:0:-1] if not str(integer)[0].isnumeric() else str(integer)[::-1] 
  integer = int(integer)
  return integer if minimum < integer < maximum else 0


if __name__ == "__main__":
  integer = 123
  print(reverseInteger(integer))

  integer = -123
  print(reverseInteger(integer))

  integer = 120
  print(reverseInteger(integer))

  integer = 0
  print(reverseInteger(integer))