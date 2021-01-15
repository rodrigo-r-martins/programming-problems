"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Follow up: Could you do this in one pass?

=> Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

=> Example 2:
Input: head = [1], n = 1
Output: []

=> Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
  The number of nodes in the list is sz.
  1 <= sz <= 30
  0 <= Node.val <= 100
  1 <= n <= sz
"""

from singlyLinkedList import SinglyLinkedList
from usefulLinkedListMethods import getListLength, printList

def removeNthNodeFromEnd(head, n):
  size = getListLength(head)
  if size == 1 and n == 1:
    return None
  if size - n == 0:
    return head.next
  i = 0
  node = head
  prev = head
  while node is not None:
      node = node.next
      i += 1
      if i == size - n:
          prev.next = node.next
          return head  
      prev = prev.next

if __name__ == "__main__":
  LL = SinglyLinkedList()
  LL.addAtHead(1)
  LL.addAtTail(2)
  LL.addAtTail(3)
  LL.addAtTail(4)
  LL.addAtTail(5)
  print("Before -> ", end="")
  print(LL)
  head = removeNthNodeFromEnd(LL.head, 2)
  print("After -> ", end="")
  printList(head)

  LL1 = SinglyLinkedList()
  LL1.addAtHead(1)
  print("Before -> ", end="")
  print(LL1)
  head = removeNthNodeFromEnd(LL1.head, 1)
  print("After -> ", end="")
  printList(head)

  LL2 = SinglyLinkedList()
  LL2.addAtHead(1)
  LL2.addAtTail(2)
  print("Before -> ", end="")
  print(LL2)
  head = removeNthNodeFromEnd(LL2.head, 1)
  print("After -> ", end="")
  printList(head)
