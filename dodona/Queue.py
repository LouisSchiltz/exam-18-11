from LinkedList import LinkedList
class Queue:
    def __init__(self):
        self.elements = LinkedList()

    def enqueue(self, element):
        self.elements.add(element)

    def dequeue(self):
        if self.getSize() == 0:
            return None
        else:
            return self.elements.removeAt(0)

    def getSize(self):
        return self.elements.__str__()

    def __str__(self):
        return self.elements.__str__()
    def IsEmpty(self):
        return self.elements.isEmpty()

