"""
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

from singlyLinkedList import SinglyLinkedList
from usefulLinkedListMethods import printList

def getReversedLinkedList(head):
  if head == None:
    return None
  prev = None
  while head:
    temp = head.next
    head.next = prev
    prev = head
    head = temp
  return prev

if __name__ == "__main__":
  LL = SinglyLinkedList()
  LL.addAtHead(1)
  LL.addAtTail(2)
  LL.addAtTail(3)
  LL.addAtTail(4)
  LL.addAtTail(5)
  head = getReversedLinkedList(LL.head)
  printList(head)