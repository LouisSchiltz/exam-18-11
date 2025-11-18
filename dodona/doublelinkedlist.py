class PersonNode:
    def __init__(self, name,age, email,prev,next):
        self.name = name
        self.age = age
        self.email = email
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_last(self,name,age,email):
        newNode = PersonNode(name,age,email,None,None)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1

    def find_by_name(self,name):
        currentNode = self.head
        index = 0
        while currentNode is not None:
            if currentNode.name == name:
                return currentNode, index

            currentNode = currentNode.next
            index += 1

        return None, -1

    def remove_by_email(self,email):
        currentNode = self.head

        while currentNode is not None:
            if currentNode.email == email:

                #case 1: removing the head
                if currentNode == self.head:
                    self.head = currentNode.next
                    if self.head is not None:
                        self.head.prev = None
                    else:
                        self.tail = None  # ← LIST IS NOW EMPTY

                #case 2: removing the tail
                elif currentNode == self.tail:
                    self.tail = currentNode.prev
                    self.tail.next = None

                #case 3: removing a node in the middle
                else:
                    currentNode.prev.next = currentNode.next
                    currentNode.next.prev = currentNode.prev

                return True #you could say here, not deleted
            currentNode = currentNode.next

        return False #node not found for ex


    def print_forward(self):
        current = self.head
        while current is not None:
            print(f"{current.name} ({current.age}) – {current.email}")
            current = current.next

    def print_backward(self):
        current = self.tail
        while current is not None:
            print(f"{current.name} ({current.age}) – {current.email}")
            current = current.prev

    def insert_after(self, name, new_name, new_age, new_email):
        current = self.head

        # search for first node with matching name
        while current is not None:
            if current.name == name:
                new_node = PersonNode(new_name, new_age, new_email)

                # case 1: inserting after the tail
                if current == self.tail:
                    current.next = new_node
                    new_node.prev = current
                    self.tail = new_node

                # case 2: inserting in the middle
                else:
                    successor = current.next
                    new_node.next = successor
                    new_node.prev = current
                    current.next = new_node
                    successor.prev = new_node

                return True  # successfully inserted

            current = current.next

        return False  # name not found





