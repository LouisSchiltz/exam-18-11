class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):   #enqeue adds an element to this queue
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self): #dequeue removes an element from this queue
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value

    def peek(self):
        if self.top is None:
            return None
        return self.top.value

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def print_stack(self):
        current = self.top
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

    def reverse_string(s, stack):
        for ch in s:
            stack.push(ch)
        result = ""
        while not stack.is_empty():
            result += stack.pop()
        return result

    def get_size(self):
        return self.size