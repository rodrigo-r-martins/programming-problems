"""
Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
It is guaranteed that the node to be deleted is not a tail node in the list.

=> Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

=> Example 2:
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

=> Example 3:
Input: head = [1,2,3,4], node = 3
Output: [1,2,4]

=> Example 4:
Input: head = [0,1], node = 0
Output: [1]

=> Example 5:
Input: head = [-3,5,-99], node = -3
Output: [5,-99]

=== Constraints ===
  The number of the nodes in the given list is in the range [2, 1000].
  -1000 <= Node.val <= 1000
  The value of each node in the list is unique.
  The node to be deleted is in the list and is not a tail node
"""

from singlyLinkedList import SinglyLinkedList
from usefulLinkedListMethods import printList

def deleteNode(head, value):
  if not head:
    return head
  if head.value == value:
    head = head.next
    return head
  
  cur = head
  while cur and cur.next:
    if cur.next.value == value:
      cur.next = cur.next.next
    else:
      cur = cur.next
  return head

if __name__ == "__main__":
  LL = SinglyLinkedList()
  LL.addAtHead(4)
  LL.addAtTail(5)
  LL.addAtTail(1)
  LL.addAtTail(9)
  value = 5
  head = deleteNode(LL.head, value)
  printList(head)

  LL = SinglyLinkedList()
  LL.addAtHead(4)
  LL.addAtTail(5)
  LL.addAtTail(1)
  LL.addAtTail(9)
  value = 1
  head = deleteNode(LL.head, value)
  printList(head)

  LL = SinglyLinkedList()
  LL.addAtHead(1)
  LL.addAtTail(2)
  LL.addAtTail(3)
  LL.addAtTail(4)
  value = 3
  head = deleteNode(LL.head, value)
  printList(head)

  LL = SinglyLinkedList()
  LL.addAtHead(0)
  LL.addAtTail(1)
  value = 0
  head = deleteNode(LL.head, value)
  printList(head)

  LL = SinglyLinkedList()
  LL.addAtHead(-3)
  LL.addAtTail(5)
  LL.addAtTail(-99)
  value = -3
  head = deleteNode(LL.head, value)
  printList(head)