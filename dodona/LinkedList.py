class Node:
    def __init__(self, element):
        self.element = element
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None   # first node in the list
        self.tail = None   # last node in the list
        self.size = 0

    def add_first(self, element):
        newNode = Node(element)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

        if self.head is None:
            self.head = newNode

    def add_last(self, element):
        newNode = Node(element)

        if self.head is None:
            self.head = newNode = self.tail
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

        self.size += 1

    def insert(self, index, element):
        if index == 0:
            self.add_first(element)
        elif index >= self.size:
            self.add_last(element)
        else:
            currentNode = self.head
            for i in range(1, index):
                currentNode = currentNode.next
            tempNode = currentNode.next
            currentNode.next = Node(element)
            currentNode.next.next = tempNode
            self.size += 1

    def removeFirst(self):
        if self.head is None:
            return None
        else:
            tempNode = self.head.element
            self.head = self.head.next
            self.size -= 1
            if self.head == None:
                self.tail = None
            return tempNode

    def removeLast(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            tempNode = self.head
            self.head = self.tail = None
            self.size = 0
            return tempNode
        else:
            currentNode = self.head
            for i in range(self.size - 2):
                currentNode = currentNode.next

            tempNode= self.tail
            self.tail = currentNode
            self.tail.next = None
            self.size -= 1
            return tempNode

    def removeAt(self,index):
        if index < 0 or index >= self.size:
            return None
        elif self.size == 0:
            return self.removeFirst()
        elif index == self.size-1:
            return self.removeLast()
        else:
            previousNode = self.head
            for i in range(1, index):
                previousNode = previousNode.next

            currentNode = previousNode.next
            previousNode.next = currentNode.next
            self.size -= 1
            return currentNode

    def getFirst(self):
        if self.head is None:
            return None
        return self.head.element

    def getLast(self):
        if self.head is None:
            return None

        current = self.head
        while current.next is not None:
            current = current.next
        return current.element

    def index_Of(self, element):
        current = self.head
        index = 0

        while current.element != element:
            if current.element == element:
                return index
            current = current.next
            index += 1

        return -1,"element not found"

    def last_index_of(self, element):
        current = self.head
        index = 0
        last_found = -1

        while current.next is not None:
            if current.element == element:
                last_found = index   #only updates last found index if current = element
            current = current.next
            index += 1

        return last_found  #returns the index of the last time the element you were looking for was in the list






#andere manier van insert @index
def insert_at_position(head, element, position):
    new_node = Node(element)
    if position == 0:
        new_node.next = head
        return new_node

    current = head
    index = 0
    while current is not None and index < position-1:
        current = current.next
        index += 1

    if current is None:
        raise IndexError('Position out of range')

    new_node.next = current.next
    current.next = new_node

    return new_node