class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_last(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1


    def InsertAt(self, element, position):
        new_node = Node(element)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
        if position > self.size:
            return "index too high"
        else:
            currentNode = self.head
            for i in range(1, position):
                currentNode = currentNode.next
            tempnode = currentNode.next
            currentNode.next = new_node
            new_node.next = tempnode
            self.size += 1

    def find(self, element):
        currentNode = self.head
        index = 0
        while currentNode is not None:
            if currentNode.element == element:
                return currentNode, index
            currentNode = currentNode.next
            index += 1
        return None, -1

    def print_list(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.element, end=" ")
            currentNode = currentNode.next

        

