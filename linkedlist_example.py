
"""
A program to calculate the sum of two polynomials through LinkedList.

    1. Take the exponents and constants as the input. 
    2. Store them and show the input variables in the form of the polynomials
    3. Show the result as the sum of the polynomials given as input.

"""

class Node:
    def __init__(self, exp, const):
        self.exp = exp
        self.const = const
        self.next = None
        

class polynomials:
    def __init__(self):
        self.head = None
    
    def insert(self, exp, coeff):
        if self.head == None:
            self.head = Node(exp, coeff)
        else:
            current_node = self.head
            newNode = Node(exp, coeff)
            newNode.next = current_node
            self.head = newNode

    def merge_sort(self, head):
        if not head or not head.next:
            return head
        
        mid_node = self.get_middle(head)
        next_to_mid = mid_node.next
        mid_node.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_mid)

        return self.merge_sorted_list(left, right)
    
    def get_middle(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def merge_sorted_list(self, left, right):
        dummy = Node(0,0)
        tail = dummy

        while left and right:
            if left.exp >= right.exp:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            
            tail = tail.next
        
        if left:
            tail.next = left
        elif right:
            tail.next = right
        
        return dummy.next
        
        """
        # Recursive Approach to sorting the linkedlist
            
        if not left:
            return right
        
        if not right:
            return left

        if left.exp >= right.exp:
            result = left
            result.next = self.merge_sorted_list(left.next, right)
        else:
            result = right
            result.next = self.merge_sorted_list(left, right.next)
    
        return result
        """

    def sort(self):
        self.head = self.merge_sort(self.head)
    
    def show_polynomial(self):
        current = self.head
        while current:
            if current.exp == 0:
                print(current.const, end=" ")
            else:
                print(f"{current.const}x^{current.exp} ", end=" ")
            if current.next:
                print("+", end=" ")
            current = current.next
        print()
    
    def sum(poly1, poly2):
        result = polynomials()
        p1 = poly1.head
        p2 = poly2.head

        while p1 and p2:
            if p2 and (not p1 or p1.exp < p2.exp):
                result.insert(p2.exp, p2.const)
                p2 = p2.next

            elif p1 and (not p2 or p1.exp > p2.exp):
                result.insert(p1.exp, p1.const)
                p1 = p1.next
            
            else:
                new_const = p1.const + p2.const
                if new_const != 0:
                    result.insert(p1.exp, new_const)
                p1 = p1.next
                p2 = p2.next
                
        return result
        


if __name__ == "__main__":
    x = polynomials()
    y = polynomials()
    
    while True:
        const = int(input("Constant: "))
        exp = int(input("Exponent: "))
        if exp == -1:
            print("Great, Done with Polynomial X. Now moving to Polynomial y")
            break
        else:
            x.insert(exp, const)
    
    while True:
        const = int(input("Constant: "))
        exp = int(input("Exponent: "))
        if exp == -1:
            print("Great, Done with Polynomial Y.")
            break
        else:
            y.insert(exp, const)
    
    x.sort()
    x.show_polynomial()
    y.sort()
    y.show_polynomial()

    result = polynomials.sum(x, y)
    result.sort()

    print("------------------------")
    print("Sum of the polynomials: ")
    result.show_polynomial()
    