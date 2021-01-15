"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:
    MyLinkedList() Initializes the MyLinkedList object.
    int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
    void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    void addAtTail(int val) Append a node of value val as the last element of the linked list.
    void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
    void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

=> Example 1:
Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation:
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3

=== Constraints ===
  0 <= index, val <= 1000
  Please do not use the built-in LinkedList library.
  At most 2000 calls will be made to get, addAtHead, addAtTail,  addAtIndex and deleteAtIndex.
"""

class Node():
  def __init__(self, value):
    self.value = value
    self.next = None


class SinglyLinkedList():
  def __init__(self):
    # Initialize your data structure here
    self.head = None
    self.length = 0

  def __repr__(self):
    current = self.head
    nodes = "List: "
    while current:
      nodes += str(current.value) + " -> "
      current = current.next
      if current is self.head:   # Detecting cycle
        break
    nodes += "None"
    return nodes

  def get(self, index):
    # Get the value of the index-th node in the linked list. If the index is invalid, return -1
    if 0 < index >= self.length:
      return -1
    current = self.head
    i = 0
    while current:
      if i == index:
        print(f"Node at index {index}: {{ value = {current.value}, next = {None if not current.next else current.next.value} }}")
        return current
      current = current.next
      i += 1
        
  def addAtHead(self, value):
    # Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list
    current = Node(value)
    self.length += 1
    if not self.head:
      self.head = current
      return
    current.next = self.head
    self.head = current
  
  def addAtTail(self, value):
    # Append a node of value val to the last element of the linked list
    current = self.head
    self.length += 1
    if not current:
      self.head = Node(value)
    else:
      while current.next:
        current = current.next
      current.next = Node(value)
      #node.next.next = self.head     # If I want to include a cycle manually
  
  def addAtIndex(self, index, value):
    # Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted
    if index > self.length:
      print("Error: index out of bounds")
      return
    if index == self.length:
      self.addAtTail(value)
      return
    if index == 0:
      self.addAtHead(value)
      return
    i = 0
    node = self.head
    prev = self.head
    while node:
      node = node.next
      i += 1
      if index == i:
        new_node = Node(value)
        new_node.next = node
        prev.next = new_node
        self.length += 1
        return
      prev = prev.next

  def deleteAtIndex(self, index):
    # Delete the index-th node in the linked list, if the index is valid
    if index >= self.length:
      print("Error: index out of bounds")
      return
    if index == 0:
      self.head = self.head.next
      self.length -= 1
      return
    i = 0
    node = self.head
    prev = self.head
    while node:
      node = node.next
      i += 1
      if index == i:
        prev.next = node.next
        self.length -= 1
        return
      prev = prev.next


if __name__ == "__main__":
  # Your LinkedList object will be instantiated and called as such:
  print("=== Example 1 ===")
  LL = SinglyLinkedList()
  LL.addAtHead(2)
  LL.deleteAtIndex(1)
  LL.addAtHead(2)
  LL.addAtHead(7)
  LL.addAtHead(3)
  LL.addAtHead(2)
  LL.addAtHead(5)
  LL.addAtTail(5)
  LL.get(5)
  print(LL)
  LL.deleteAtIndex(6)
  print(LL)
  LL.deleteAtIndex(4)
  print(LL)
  LL.get(3)
  LL.get(4)
  print(f"List Length: {LL.length}")

  print("\n=== Example 2 ===")
  LL_2 = SinglyLinkedList()
  LL_2.addAtHead(1)
  LL_2.deleteAtIndex(0)
  print(LL_2)
  print(f"List Length: {LL_2.length}")
