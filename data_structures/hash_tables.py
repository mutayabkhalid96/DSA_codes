# creating a hashtable

"""
Here we have used __ before and after the function names. This allows us to call get set functions without specifying them. 
Python knows which function to call when a certain command is called. 

class MyClass:
    def __init__(self, value):
        self.value = value

    def __len__(self):
        return self.value

# Create an instance
obj = MyClass(5)

# Calling len() on obj
# Python sees len(obj) and looks for obj.__len__()
print(len(obj))  # Output: 5, since __len__ is defined to return self.value

In this example:

    You call len(obj).
    Python knows len() corresponds to __len__, so it looks for an __len__ method in obj.
    It finds obj.__len__() and calls it, returning the result.
"""

class HashTablewithoutcollisions:
  def __init__(self):
    self.size = 100
    self.array = [[] for i in range(self.size)]

  def get_hashkey(self, key):
    if type(key) == int:
      return key % self.size
    else:
      total = 0
      for i in key:
        total += ord(i)
      return total % self.size

  def __setitem__(self, key, value):
    hashkey = self.get_hashkey(key)

    found = False

    for idx, element in enumerate(self.array[hashkey]):
      if len(element) ==2 and element[0] == key:
        self.array[hashkey][idx] = (key, value)
        found = True
        break
      if not found:
        self.array[hashkey].append((key, value))

  def __getitem__(self, key):
    hashkey = self.get_hashkey(key)
    for element in self.array[hashkey]:
      if element[0] == key:
        return element[1]
    return self.array[hashkey]
