"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

=> Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

=== Note ===
  1 <= A.length <= 5000
  0 <= A[i] <= 5000
"""

def sortArrayByParity(A):
  # position = 0
  # for i in range(len(A)):
  #   if A[i] % 2 == 0:
  #     A[position], A[i] = A[i], A[position]
  #     position += 1
  # return A

  A.sort(key=lambda x: x%2)
  return A

if __name__ == "__main__":
  A = [3,1,2,4]
  print(sortArrayByParity(A))