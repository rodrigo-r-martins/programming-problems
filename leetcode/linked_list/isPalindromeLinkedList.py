"""
Given a singly linked list, determine if it is a palindrome.

=> Example 1:
Input: 1->2
Output: false

=> Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
"""

from singlyLinkedList import SinglyLinkedList
from usefulLinkedListMethods import printList

def isPalindromeLinkedList(head):
  nodes = []
  cur = head
  while cur:
    nodes.append(str(cur.value))
    cur = cur.next
  #nodes_str = "".join(nodes)
  #print(nodes_str)
  #nodes.reverse()
  #nodes_str_rev = "".join(nodes)
  #print(nodes_str_rev)
  if nodes == nodes[::-1]:
    return True  
  return False


if __name__ == "__main__":
  LL = SinglyLinkedList()
  LL.addAtHead(1)
  LL.addAtTail(2)
  printList(LL.head)
  print(isPalindromeLinkedList(LL.head))

  LL_1 = SinglyLinkedList()
  LL_1.addAtHead(1)
  LL_1.addAtTail(2)
  LL_1.addAtTail(2)
  LL_1.addAtTail(1)
  printList(LL_1.head)
  print(isPalindromeLinkedList(LL_1.head))