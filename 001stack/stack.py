class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty. Cannot pop from an empty stack.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

def main():
    # Create a new stack
    stack = Stack()

    # Check if the stack is empty
    print(stack.is_empty())  # Output: True

    # Push elements onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Check the size of the stack
    print(stack.size())  # Output: 3

    # Peek the top element (last element added) without removing it
    print(stack.peek())  # Output: 30

    # Pop elements from the stack
    print(stack.pop())  # Output: 30
    print(stack.pop())  # Output: 20

    # Check the size of the stack after popping elements
    print(stack.size())  # Output: 1

    # Pop the last element from the stack
    print(stack.pop())  # Output: 10

    # Check if the stack is empty after popping all elements
    print(stack.is_empty())  # Output: True

if __name__ == "__main__":
    main()
