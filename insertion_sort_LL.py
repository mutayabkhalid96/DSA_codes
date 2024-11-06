class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end= " ")
            if current.next:
                print("->", end=" ")
            current = current.next
        print()
    
    def sort(self):
        print("Sorting the list. Vänta lite!")
        self.head = self.insertion_sort(self.head)
        self.display()
    
    def insertion_sort(self, head):
        sorted_head = None
        current_node = head

        while current_node:
            next_node = current_node.next
            sorted_head = self.sortedlist(sorted_head, current_node)
            current_node = next_node
        
        return sorted_head
    
    def sortedlist(self, head, node):
        if head is None or node.data <= head.data:
            node.next = head
            return node
        
        current = head
        while current.next and node.data > current.next.data:
            current = current.next
        
        node.next = current.next
        current.next = node

        return head

if __name__ == "__main__":
    l1 = Linkedlist()
    while True:
        userin = int(input("Enter -1 to stop: "))
        if userin == -1:
            break
        else:
            l1.insert(userin)
    l1.display()
    l1.sort()