class Stack:
    def __init__(self):
        self.__elements = []

    def isEmpty(self):
        return len(self.__elements) == 0

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements.pop()

    def peek(self):
        if self.isEmpty():
            return None
        else: return self.__elements[len(self.__elements) - 1]

    def getSize(self):
        return len(self.__elements)


