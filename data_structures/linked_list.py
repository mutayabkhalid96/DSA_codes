
"""
"""

class Node:
  def __init__(self, value):
    self.data = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def print_list(self):
    if self.head == None:
      print("Linked List is Empty")
      return
    else:
      itr = self.head
      while itr:
        print(itr.data)
        itr = itr.next

  def insert_at(self, data, index):
    if self.head == None:
      self.head = Node(data)
      return
    else:
      itr = self.head
      count = 0
      while itr.next:
        if count == index - 1:
          new_node = Node(data)
          new_node.next = itr.next
          itr.next = new_node
          break
        itr = itr.next
        count += 1

  def remove_at(self, index):
    if self.head == None:
      print("Linked List is empty.")
      return
    else:
      itr = self.head
      count = 0
      while itr.next:
        if count  == index - 1:
          itr.next = itr.next.next
          break
        itr = itr.next
        count += 1

  def insert_at_end(self, value):
    if self.head == None:
      self.head = Node(value)
      return
    else:
      itr = self.head
      while itr.next:
        itr = itr.next
      new_node = Node(value)
      itr.next = new_node

  def insert_values(self, datalist):
    if self.head != None:
      #print("Linked list already filled. Please use relevant functions to add values")
      raise Exception("Invalid request")
    else:
      for data in datalist:
        self.insert_at_end(data)
