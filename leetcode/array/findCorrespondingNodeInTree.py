"""
Given two binary trees original and cloned and given a reference to a node target in the original tree.
The cloned tree is a copy of the original tree.
Return a reference to the same node in the cloned tree.
Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.
Follow up: Solve the problem if repeated values on the tree are allowed.

=> Example 1:
Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.

=> Example 2:
Input: tree = [7], target =  7
Output: 7

=> Example 3:
Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4

=> Example 4:
Input: tree = [1,2,3,4,5,6,7,8,9,10], target = 5
Output: 5

=> Example 5:
Input: tree = [1,2,null,3], target = 2
Output: 2

=== Constraints ===

  The number of nodes in the tree is in the range [1, 10^4].
  The values of the nodes of the tree are unique.
  target node is a node from the original tree and is not null.
"""

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

def insertNode(root, x):
  if root is None:
    return TreeNode(x)
  else:
    if root.val == x:
      return root
    elif root.val < x:
      root.right = insertNode(root.right, x)
    else:
      root.left = insertNode(root.left, x)
    return root

def inorderTraversal(root):
  if root:
    inorderTraversal(root.left)
    print(root.val)
    inorderTraversal(root.right)

# Functions used on LeetCode problem
def inorderTraversalLeetcode(root):
  if not original_tree:
    return None
  if original_tree == target:
    return cloned_tree
  return inorderTraversal(original_tree.left, cloned_tree.left, target) or inorderTraversal(original_tree.right, cloned_tree.right, target)

def findCorrespondingNode(original_tree, cloned_tree, target):
  return inorderTraversal(original_tree, cloned_tree, target)


if __name__ == "__main__":
  values = [4, 3, None, None, 6, 19]
  target = 3

  original_tree = TreeNode(7)
  cloned_tree = TreeNode(7)
  for x in values:
    if x is not None:
      original_tree = insertNode(original_tree, x)
      cloned_tree = insertNode(cloned_tree, x)
  
  inorderTraversal(original_tree)
