"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

=> Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

=> Example 2:
Input: l1 = [], l2 = []
Output: []

=> Example 3:
Input: l1 = [], l2 = [0]
Output: [0]

=== Constraints ===
  The number of nodes in both lists is in the range [0, 50].
  -100 <= Node.val <= 100
  Both l1 and l2 are sorted in non-decreasing order.
"""

from doublyLinkedList import DoublyLinkedList
from usefulLinkedListMethods import printList

def mergeTwoSortedLists(l1, l2):
  if not l1:
    return l2
  if not l2:
    return l1
  if not l1 and not l2:
    return None
  ll = DoublyLinkedList()
  cur_l1 = l1.head
  cur_l2 = l2.head
  index = 0
  max_length = l1.length + l2.length
  while index < max_length:
    if cur_l1 and cur_l2:
      if cur_l1.value <= cur_l2.value:
        ll.addAtIndex(index, cur_l1.value)
        cur_l1 = cur_l1.next
      else:
        ll.addAtIndex(index, cur_l2.value)
        cur_l2 = cur_l2.next
    elif cur_l1 and not cur_l2:
      ll.addAtIndex(index, cur_l1.value)
      cur_l1 = cur_l1.next
    elif cur_l2 and not cur_l1:
      ll.addAtIndex(index, cur_l2.value)
      cur_l2 = cur_l2.next
    index += 1
  return ll

if __name__ == "__main__":
  LL1 = DoublyLinkedList()
  LL1.addAtHead(1)
  LL1.addAtTail(2)
  LL1.addAtTail(4)
  print(LL1)

  LL2 = DoublyLinkedList()
  LL2.addAtHead(1)
  LL2.addAtTail(3)
  LL2.addAtTail(4)
  print(LL2)

  print(mergeTwoSortedLists(LL1, LL2))
  