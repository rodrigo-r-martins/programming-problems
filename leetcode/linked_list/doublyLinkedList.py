"""
In this article, we will introduce another type of linked list: Doubly Linked List.

=> Definition:
The doubly linked list works in a similar way but has one more reference field which is known as the "prev" field. With this extra field, you are able to know the previous node of the current node.

=> We will use the head node to represent the whole list.
"""

class Node():
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None


class DoublyLinkedList():
  def __init__(self):
    # Constructor
    self.head = None
    self.length = 0
  
  def __repr__(self):
    # Print LinkedList
    node = self.head
    nodes = "List: "
    while node:
      nodes += str(node.value) + " -> "
      node = node.next
      if node is self.head:   # Detecting cycle
        return
    nodes += "None"
    return nodes

  def get(self, index):
    # Get the value of the index-th node in the linked list. If the index is invalid, return -1
    if 0 < index >= self.length:
      return -1
    node = self.head
    i = 0
    while node:
      if i == index:
        print(f"Node at index {index}: {{ value = {node.value}, prev = {None if not node.prev else node.prev.value}, next = {None if not node.next else node.next.value} }}")
        return node
      node = node.next
      i += 1
        
  def addAtHead(self, value):
    # Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list
    new_node = Node(value)
    head = self.head
    self.length += 1
    if not head:
      self.head = new_node
      return
    new_node.next = head
    head.prev = new_node
    self.head = new_node
  
  def addAtTail(self, value):
    # Append a node of value val to the last element of the linked list
    new_node = Node(value)
    current = self.head
    self.length += 1
    if not current:
      self.head = new_node
      return
    while current.next:
      current = current.next
    current.next = new_node
    new_node.prev = current
    #node.next.next = self.head     # If I want to include a cycle manually
  
  def addAtIndex(self, index, value):
    '''
    If we want to insert a new node cur after an existing node prev, we can divide this process into two steps:
      - link cur with prev and next, where next is the original next node of prev;
      - re-link the prev and next with cur. 
    Similar to the singly linked list, both the time and the space complexity of the add operation are O(1).
    '''
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
    current = self.head
    while current:
      current = current.next
      i += 1
      if index == i:
        new_node = Node(value)
        new_node.next = current
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node
        self.length += 1
        return

  def deleteAtIndex(self, index):
    '''
    If we want to delete an existing node cur from the doubly linked list, we can simply link its previous node prev with its next node next.
    Unlike the singly linked list, it is easy to get the previous node in constant time with the "prev" field.
    Since we no longer need to traverse the linked list to get the previous node, both the time and space complexity are O(1).
    '''
    # Delete the index-th node in the linked list, if the index is valid
    if index >= self.length:
      print("Error: index out of bounds")
      return
    if index == 0:
      self.head = self.head.next
      self.length -= 1
      return
    i = 0
    current = self.head
    while current:
      current = current.next
      i += 1
      if index == i:
        current.prev.next = current.next
        if current.next:
          current.next.prev = current.prev
        current = None
        self.length -= 1
        return


if __name__ == "__main__":
  # Your LinkedList object will be instantiated and called as such:
  print("=== Example 1 ===")
  LL = DoublyLinkedList()
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
  LL_2 = DoublyLinkedList()
  LL_2.addAtHead(1)
  LL_2.deleteAtIndex(0)
  print(LL_2)
  print(f"List Length: {LL_2.length}")


