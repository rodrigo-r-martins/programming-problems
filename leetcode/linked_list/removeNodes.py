"""
Remove all elements from a linked list of integers that have value val.

=> Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

from singlyLinkedList import SinglyLinkedList
from usefulLinkedListMethods import printList

def removeNodes(head, value):
  if not head:
    return head
  while head and head.value == value:
    head = head.next
  cur = head
  while cur and cur.next:
    if cur.next.value == value:
      cur.next = cur.next.next
    else:
      cur = cur.next
  return head

if __name__ == "__main__":
  LL = SinglyLinkedList()
  LL.addAtHead(1)
  LL.addAtTail(6)
  LL.addAtTail(3)
  LL.addAtTail(4)
  LL.addAtTail(5)
  LL.addAtTail(6)
  value = 6
  head = removeNodes(LL.head, value)
  printList(head)