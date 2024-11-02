
"""
## Stack
The stack implementation is similar to when your browser stores the history of the pages that you have visited recently. This implementation is done in stack.

"""

from collections import deque

class Stack:
  def __init__(self):
    self.container = deque()

  def push(self, value):
    self.container.append(value)

  def pop(self):
    return self.container.pop()

  def peak(self):
    return self.container[-1]

  def pop_all(self):
    for i in range(len(self.container)):
      print (self.container.pop())

  def is_emppty(self):
    return len(self.container)  == 0