"""
# Binary Tree
A specific tree whose child always at max two nodes.

##Binary Search Tree
A specific type of the binary tree where LHS of each node has always value smaller than the value in the parent node. 
RHS of each node has a value greater than the value in the node itself.

"""

class BinarySearchTree:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def add_child(self, data):
    "Add the child to left hand side"
    if self.data == data:
      return

    if data < self.data:
      if self.left:
        self.left.add_child(data)
      else:
        self.left = BinarySearchTree(data)

    "Add the child to the right hand side"
    if data > self.data:
      if self.right:
        self.right.add_child(data)
      else:
        self.right = BinarySearchTree(data)

  def inorder_traversal(self):
    elements = []
    if self.left:
     elements += self.left.inorder_traversal()

    elements.append(self.data)

    if self.right:
      elements += self.right.inorder_traversal()

    return elements

  def inorder_traversal_alone(self, root):
      if root is None:
        return []
      return self.inorder_traversal_alone(root.left) + [root.data] + self.inorder_traversal_alone(root.right)

  def search_tree(self, value):
    if self.data == value:
      return True

    if value < self.left:
      return self.left.search_tree(value)
    else:
      return False

    if value > self.right:
      return self.right.search_tree(value)
    else:
      return False

  def find_min(self):
    if self.left is None:
      return self.data
    else:
      return self.left.find_min()

    #inorder_tree = self.inorder_traversal()
    #return inorder_tree[0]

  def find_max(self):
    if self.right is None:
      return self.data
    else:
      return self.right.find_max()
    # inorder_tree = self.inorder_traversal()
    # return inorder_tree[-1]

  def find_sum(self):
    left_sum = self.left.find_sum() if self.left else 0
    right_sum = self.right.find_sum() if self.right else 0
    return self.data + left_sum + right_sum
    # inorder_tree = self.inorder_traversal()
    # return sum(inorder_tree)

  def postorder_traversal(self):
    elements = []
    if self.left:
      elements += self.left.postorder_traversal()
    if self.right:
      elements += self.right.postorder_traversal()
    elements.append(self.data)
    return elements

  def preorder_traversal(self):

    elements = []
    elements.append(self.data)
    if self.left:
      elements += self.left.preorder_traversal()
    if self.right:
      elements += self.right.preorder_traversal()

    return elements

  def delete_node(self, val):
      if val < self.data:
        if self.left:
          self.left = self.left.delete_node(val)
      elif val > self.data:
        if self.right:
          self.right = self.right.delete_node(val)
      else:
      # if there is no child
        if self.left is None and self.right is None:
          return None

        # if there is one child either left or right
        elif self.left is None:
          return self.right
        elif self.right is None:
          return self.left
        # if there is a sub-tree below the node to be deleted
        min_val = self.left.find_max()
        self.data = min_val
        self.left = self.left.delete_node(min_val)

      return self


def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
      root.add_child(elements[i])

    return root