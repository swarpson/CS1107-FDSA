class Node:
    def __init__(self, data):  
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):  
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()  # for newline at the end

# Test 1: Insert 10 at the beginning, then 20, then 30
ll1 = LinkedList()
ll1.insert_at_beginning(10)
ll1.insert_at_beginning(20)
ll1.insert_at_beginning(30)
print("Linked List after insertions at the beginning:")
ll1.traverse()  # Expected Output: 30 -> 20 -> 10  

# Test 2: Insert 5 at the end, then 10, 15, and 20
ll2 = LinkedList()
ll2.insert_at_end(5)
ll2.insert_at_end(10)
ll2.insert_at_end(15)
ll2.insert_at_end(20)
print("Linked List after insertions at the end:")
ll2.traverse()  # Expected Output: 5 -> 10 -> 15 -> 20


# Test 3: Insert 10, 20, 30, 40 at the end, then delete node with data 20
ll3 = LinkedList()
ll3.insert_at_end(10)
ll3.insert_at_end(20)
ll3.insert_at_end(30)
ll3.insert_at_end(40)
ll3.delete_node(20)
print("Linked List after deletion of node with data 20:")
ll3.traverse()  # Expected Output: 10 -> 30 -> 40
