def getListLength(head):
  # If LinkedList doesn't have the length attribute we use this recursive function to get the List size
  if head == None:
      return 0
  return 1 + getListLength(head.next)

def printList(head):
  node = head
  nodes = "List: "
  if getListLength(head) == 0:
    nodes += "None"
    print(nodes)
  elif getListLength(head) == 1:
    nodes += str(head.value)
    print(nodes)
  else:
    while node is not None:
      nodes += str(node.value) + " -> "
      node = node.next
    nodes += "None" 
    print(nodes)