class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

def main():
    # Create a new linked list
    linked_list = LinkedList()

    # Append elements to the linked list
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    # Display the linked list
    linked_list.display()  # Output: 10 -> 20 -> 30 -> None

    # Prepend an element to the linked list
    linked_list.prepend(5)

    # Display the linked list after prepending
    linked_list.display()  # Output: 5 -> 10 -> 20 -> 30 -> None

    # Search for an element in the linked list
    print(linked_list.search(20))  # Output: True
    print(linked_list.search(40))  # Output: False

    # Delete an element from the linked list
    linked_list.delete(10)

    # Display the linked list after deleting
    linked_list.display()  # Output: 5 -> 20 -> 30 -> None


if __name__ == "__main__":
    main()
