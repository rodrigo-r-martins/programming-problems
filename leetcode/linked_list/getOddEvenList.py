"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

=> Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

=> Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

=== Constraints ===
  The relative order inside both the even and odd groups should remain as it was in the input.
  The first node is considered odd, the second node even and so on ...
  The length of the linked list is between [0, 10^4].
"""

from singlyLinkedList import SinglyLinkedList
from usefulLinkedListMethods import printList

def getOddEvenList(head):
  if not head:
    return head
  cur = head
  pos = 0
  evens = []
  odds = []
  while cur:
    if pos % 2 == 0:
      evens.append(cur.value)
    else:
      odds.append(cur.value)
    pos += 1
    cur = cur.next
  LL = SinglyLinkedList()
  while evens:
    LL.addAtTail(evens[0])
    evens.pop(0)
  while odds:
    LL.addAtTail(odds[0])
    odds.pop(0)
  return LL.head


if __name__ == "__main__":
  LL = SinglyLinkedList()
  LL.addAtHead(1)
  LL.addAtTail(2)
  LL.addAtTail(3)
  LL.addAtTail(4)
  LL.addAtTail(5)
  head = getOddEvenList(LL.head)
  printList(head)

  LL_1 = SinglyLinkedList()
  LL_1.addAtHead(2)
  LL_1.addAtTail(1)
  LL_1.addAtTail(3)
  LL_1.addAtTail(5)
  LL_1.addAtTail(6)
  LL_1.addAtTail(4)
  LL_1.addAtTail(7)
  head = getOddEvenList(LL_1.head)
  printList(head)