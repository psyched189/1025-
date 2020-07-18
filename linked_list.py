## TODO: Add Palindrome Checker function - it includes both - i) Finding Middle node, and ii) Reversing a LinkedList

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def append(self, data): #insert at end
        
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
            
        curr.next = new_node
    
    def push(self, data): #insert at start
        
        new_node = Node(data)
        
        head = self.head
        self.head = new_node
        new_node.next = head
        
    def insert_after_val(self, val, data): 
        
        new_node = Node(data)
        
        curr = self.head
        while curr and curr.data != val:
            curr = curr.next
            
        if not curr:
            print('Given val not in LL')
            return
        
        next_ = curr.next
        curr.next = new_node
        new_node.next = next_
        
    def insert_before_val(self, val, data):
        
        new_node = Node(data)
        
        prev = None
        curr = self.head
        while curr and curr.data != val:
            prev = curr
            curr = curr.next
        
        if not curr:
            print('Given value not in LL')
            return
        
        if not prev:
            self.head = new_node
            new_node.next = curr
            return
        
        prev.next = new_node
        new_node.next = curr
        
    def remove(self): #remove from end
        
        prev = None
        curr = self.head
        while curr.next:
            prev = curr
            curr = curr.next
        if not prev:
            self.head = None
            return
        
        prev.next = None
        
    def pop(self): #remove first(head)
        
        head = self.head
        if not head:
            print('LL empty')
            return
        
        self.head = head.next
        
        
    def swap_by_val(self, a, b):
        
        if a == b:
            print('Values equal - LL unchanged')
            return
    
        prev_a = None
        curr_a = self.head
        while curr_a and curr_a.data != a:
            prev_a = curr_a
            curr_a = curr_a.next
        
        prev_b = None
        curr_b = self.head
        while curr_b and curr_b.data != b:
            prev_b = curr_b
            curr_b = curr_b.next
        
        if not curr_a or not curr_b:
            print('One or both of the given values not in LL')
            return
        
        if prev_a:
            prev_a.next = curr_b
        else:
            self.head = curr_b

        if prev_b:
            prev_b.next = curr_a
        else:
            self.head = curr_a
        
        curr_a.next, curr_b.next = curr_b.next, curr_a.next

        
    def swap_by_pos(self, a, b):
        
        if a == b:
            print('Already at the required position - LL unchanged')
            return
    
        prev_a = None
        curr_a = self.head
        count_a = 0
        while curr_a and count_a != a:
            prev_a = curr_a
            curr_a = curr_a.next
            count_a += 1
        
        prev_b = None
        curr_b = self.head
        count_b = 0
        while curr_b and count_b != b:
            prev_b = curr_b
            curr_b = curr_b.next
            count_b += 1
            
        if not curr_a or not curr_b:
            print('One or both of the given values not in LL')
            return
        
        if prev_a:
            prev_a.next = curr_b
        else:
            self.head = curr_b

        if prev_b:
            prev_b.next = curr_a
        else:
            self.head = curr_a
        
        curr_a.next, curr_b.next = curr_b.next, curr_a.next
        
        
    def find(self, val):
        
        curr = self.head
        if curr.data == val:
            print(f'Val {val} found at position 0')
            return
        
        count = 0
        while curr and curr.data != val:
            curr = curr.next
            count += 1
            
        if not curr:
            print(f'Val {val} not in LL')
            return
        
        print(f'Val {val} found at position {count}')
        
        
    def remove_val(self, val):
        
        prev = None
        curr = self.head
        
        while curr and curr.data != val:
            prev = curr
            curr = curr.next
            
        if not curr:
            print(f'Val {val} not in LL')
            return
        if not prev:
            self.head = curr.next
            return
        prev.next = curr.next
        
        
    def remove_k_from_end_bt(self, k):

        trav = self.head
        
        size = 0 
        while trav:
            trav = trav.next
            size += 1
        nth = size - k
        prev = None
        curr = self.head
        count = 0
        while  curr and count!= nth:
            prev = curr
            curr = curr.next
            count += 1
            
        if not curr:
            return 
        
        if not prev:
            first = self.head
            self.head = first.next
            return
    
        prev.next = curr.next
    

    def remove_k_from_end(self, k):

        first = self.head
        second = self.head

        for i in range(k):
            first = first.next

        if not first:
            self.head = second.next
            return

        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next


    def _print(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
        print('\n')
        
        
ll = LinkedList()
ll.append(2)
ll.append(4)
ll.append(6)
ll.append(7)
ll.append(8)
ll._print()
ll.swap_by_val(8,2)
ll._print()
ll.swap_by_pos(0,4)
ll._print()
ll.push(1)
ll._print()
ll.insert_after_val(2,3)
ll._print()
ll.insert_before_val(6,5)
ll._print()
ll.remove()
ll._print()
ll.pop()
ll._print()
ll.find(7)
print('\n')
ll.remove_val(2)
ll._print()
ll.remove_k_from_end_bt(5)
ll._print()
ll.remove_k_from_end(3)
ll._print()
