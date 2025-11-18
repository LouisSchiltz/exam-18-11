class TaskNode:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.next = None


class Tasklist:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_task(self, name, priority):
        new_node = TaskNode(name, priority)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def reorder_by_priority(self):
        #rebuilds the pieces in the correct order/sorts them
        def insert_sorted(head, node):
            if head is None or node.priority <= head.priority:
                node.next = head
                return node
            head.next = insert_sorted(head.next, node)  #.next is basically the same as n+1
            return head

        # breaks the list apart piece by piece
        def sort_recursive(head):
            if head is None or head.next is None:
                return head
            first = head
            rest = head.next
            first.next = None   #this disconnects the node from the list
            sorted_rest = sort_recursive(rest)
            return insert_sorted(sorted_rest, first) #we re-enter the node we took of in order to order the 'rest'

        # call the recursive sorter on the current list
        self.head = sort_recursive(self.head)


        #sort recursive=>   #Take the first book off the pile.
                            #Recursively sort the rest.
                            #When the rest is sorted, put this book back in the right place.