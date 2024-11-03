from collections import deque

class queue:
  def __init__(self):
    self.buffer = deque()

  def enqueue(self, val):
    self.buffer.appendleft(val)

  def dequeue(self):
    return self.buffer.pop()

  def queuelen(self):
    return len(self.buffer)

  def front(self):
    return self.buffer[-1]

  def rear(self):
    return self.buffer[0]