class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Append node at the end
    def append_node(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty, make new node the head
            self.head = new_node
        else:
            last = self.head
            while last.next:  # Traverse to the last node
                last = last.next
            last.next = new_node  # Link the new node at the end

    # 2. Search for a node with a particular value
    def search_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True  # Data found
            current = current.next
        return False  # Data not found

    # 3. Display the list
    def display_list(self):
        current = self.head
        if not current:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()  # For new line at the end


# Test the operations

# Create a linked list
ll = SinglyLinkedList()

# Append nodes to the list
ll.append_node(10)
ll.append_node(20)
ll.append_node(30)

print("List after appending nodes:")
ll.display_list()  # Expected output: 10 -> 20 -> 30

# Search for a node with data 20
print("Search for node with data 20:", "Found" if ll.search_node(20) else "Not Found")  # Expected output: Found

# Search for a node with data 50
print("Search for node with data 50:", "Found" if ll.search_node(50) else "Not Found")  # Expected output: Not Found
