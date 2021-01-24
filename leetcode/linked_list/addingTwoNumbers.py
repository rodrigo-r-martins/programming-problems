"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

=> Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

=> Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

=> Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

=== Constraints ===
  The number of nodes in each linked list is in the range [1, 100].
  0 <= Node.val <= 9
  It is guaranteed that the list represents a number that does not have leading zeros.
"""

from doublyLinkedList import DoublyLinkedList
from usefulLinkedListMethods import printList

def addingTwoNumbers(l1, l2):
  l1_values = []
  l2_values = []
  while l1.head or l2.head:
    if l1.head:
      l1_values.append(str(l1.head.value))
      l1.head = l1.head.next
    if l2.head:
      l2_values.append(str(l2.head.value))
      l2.head = l2.head.next
  
  sum_result = int("".join(l1_values[::-1])) + int("".join(l2_values[::-1]))
  sum_result = list(str(sum_result))
  
  ll = DoublyLinkedList()
  index = 0
  for i in range(len(sum_result)-1, -1, -1):
    ll.addAtIndex(index, sum_result[i])
    index += 1
  return ll


if __name__ == "__main__":
  LL1 = DoublyLinkedList()
  LL1.addAtHead(2)
  LL1.addAtTail(4)
  LL1.addAtTail(9)
  print(LL1)

  LL2 = DoublyLinkedList()
  LL2.addAtHead(5)
  LL2.addAtTail(6)
  LL2.addAtTail(4)
  LL2.addAtTail(9)
  print(LL2)

  print(addingTwoNumbers(LL1, LL2))

  LL3 = DoublyLinkedList()
  LL3.addAtHead(9)
  LL3.addAtTail(9)
  LL3.addAtTail(9)
  LL3.addAtTail(9)
  LL3.addAtTail(9)
  LL3.addAtTail(9)
  LL3.addAtTail(9)
  print(LL3)

  LL4 = DoublyLinkedList()
  LL4.addAtHead(9)
  LL4.addAtTail(9)
  LL4.addAtTail(9)
  LL4.addAtTail(9)
  print(LL4)

  print(addingTwoNumbers(LL3, LL4))