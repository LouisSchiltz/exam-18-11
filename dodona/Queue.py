class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.front is None:
            return None
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return value

    def peek(self):
        if self.front is None:
            return None
        return self.front.value

    def is_empty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def print_queue(self):
        current = self.front
        while current:
            print(current.value, end=" ")
            current = current.next
        print()


