
"""
# Trees: General Tree
A tree data structure is a recursive data structure where we begin with a root node 
and then followed by the branches or also leave nodes. 
In other words, it is also called parent and children node forms 
where each node having further nodes connected to it as parent children hirerarichal structure.

"""
class TreeNode:
  def __init__(self, name, designation):
    self.name = name
    self.designation = designation
    self.children = []
    self.parent = None

  def add_child(self, child):
    child.parent = self
    self.children.append(child)

  def get_level(self):
    level = 0
    current_parent = self.parent
    while current_parent:
      level += 1
      current_parent = current_parent.parent
    return level

  def print_tree(self, choice, level_req):
    if choice == "designation":
      value = self.designation

    if choice == "both":
      value = self.name + "(" + self.designation + ")"
    else:
      value = self.name

    if self.get_level() > level_req:
      return

    spaces = " " * self.get_level() * 3
    print(spaces + value)
    for child in self.children:
      child.print_tree(choice, level_req)


root = TreeNode("Khalid & Adeeba", "Parents")
child1 = TreeNode("Mutayab", "Eldest Son")
child2 = TreeNode("Bareera", "Daughter")
child3 = TreeNode("Faizan", "Younger Son")
child4 = TreeNode("Abdullah", "Youngest Son")

child11 = TreeNode("Saad", "Mutayab's Son")
child12 = TreeNode("Khadija", "Mutayab's Daughter")

child21 = TreeNode("Maryam", "bareera's Daughter")
child22 = TreeNode("Zaid", "bareera's Son")


root.add_child(child1)
root.add_child(child2)
root.add_child(child3)
root.add_child(child4)

child1.add_child(child11)
child1.add_child(child12)

child2.add_child(child22)
child2.add_child(child21)

root.print_tree("name", 1)
print("----------------------")

root = TreeNode("Global", "World")

count1 = TreeNode("India",    "Country")
count2 = TreeNode("USA",      "Country")
count3 = TreeNode("Pakistan", "Country") 

city11 = TreeNode("Gujrat",     "State")
city12 = TreeNode("Karnataka",  "State")
city21 = TreeNode("Florida",    "State")
city31 = TreeNode("Punjab",     "State")

city111 = TreeNode("Ahmedadbad", "City")
city121 = TreeNode("Mysore",     "City ")

city211 = TreeNode("Princeton", None)
city311 = TreeNode("Lahore", None)

root.add_child(count1)
root.add_child(count2)
root.add_child(count3)

count1.add_child(city11)
count1.add_child(city12)
city11.add_child(city111)
city12.add_child(city121)

count2.add_child(city21)
city21.add_child(city211)

count3.add_child(city31)
city31.add_child(city311)

root.print_tree("name", 2)