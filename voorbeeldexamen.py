from asyncio import tasks

class Tasks:
    def __init__(self, task_name, duration, priority):
        self.task_name = task_name
        self.duration = duration
        self.priority = priority
        self.next = None
        self.prev = None

class FactoryProduction:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_task(self, task_name, duration, priority):
        new_task = Tasks(task_name, duration, priority)
        if self.head is None:
            self.head = self.tail = new_task
        else:
            self.tail.next = new_task
            self.tail = new_task
            new_task.prev = self.tail

        self.size += 1

    def remove_task(self, task_name):
        current_task = self.head
        while current_task is not None:
            if current_task.task_name == task_name:

                if current_task == self.head:
                    self.head = current_task.next
                    if self.head is not None:
                        self.head.prev = None
                    else:
                        self.tail = None

                elif current_task == self.tail:
                    self.tail = current_task.prev
                    if self.tail is not None:
                        self.tail.next = None
                    else:
                        self.head = None

                else:
                    current_task.prev.next = current_task.next
                    current_task.next.prev = current_task.prev

                self.size -= 1
                return 'task removed'

            current_task = current_task.next
        return False

    def display_tasks(self):
        current_task = self.head
        while current_task is not None:
            print(f"{current_task.task_name} : {current_task.duration} : {current_task.priority}")
            current_task = current_task.next

    def find_task(self, task_name):
        current_task = self.head
        while current_task is not None:
            if current_task.task_name == task_name:
                return current_task.task_name, current_task.duration, current_task.priority

            current_task = current_task.next

        return None, None, None

    def calculate_total_duration(self):
        current_task = self.head
        total_duration = 0
        while current_task is not None:
            total_duration += current_task.duration
            current_task = current_task.next

        return total_duration

    def read_tasks_from_csv(self, file_path):
        tekst = open(file_path, 'r')
        tekst = tekst.readlines()         #creates list with elements(these were the lines from the csv file)
        for i in range(1, len(tekst)):     #loops over all elements in the list starting from element 1(line 1), skip header
            node = tekst[i].split(',')     #splits each line at the comma, creating a list with each field
            node[2] = node[2].replace('\n', '')  #removes the new line ch from the last line
            task_name = node[0]
            duration = int(node[1])     #extract the values
            priority = int(node[2])
            self.add_task(task_name, duration, priority)  #adds the task to a node

    def reorder_tasks_by_priority(self):
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

#--------------------------------------------------------------------------------------------
    def reorder_tasks_by_priority_duration(self):
        inpoet = None
        current = self.head
        while current is not None:
            inpoet = self.sorted_insert_by_priority_duration(inpoet, current)
            current = current.next
        resultaat = FactoryProduction()
        while inpoet is not None:
            resultaat.add_task(inpoet.task_name, inpoet.duration, inpoet.priority)
            inpoet = inpoet.next
        return resultaat

    def sorted_insert_by_priority_duration(self, head, node):
        newNode = Tasks(node.task_name, node.duration, node.priority)

        if head is None:
            head = newNode
            return head
        if newNode.priority < head.priority:
            newNode.next = head
            head = newNode
            return head
        if newNode.priority == head.priority:
            if newNode.duration < head.duration:
                newNode.next = head
                head = newNode
                return head

        previous = head
        while previous.next is not None and newNode.priority > previous.next.priority:
            previous = previous.next

        if previous.next is None:
            previous.next = newNode
            return head

        while previous.next is not None and previous.next.priority == newNode.priority and newNode.duration > previous.next.duration:
            previous = previous.next

        if previous.next is None:
            previous.next = newNode
        else:
            temp = previous.next
            previous.next = newNode
            newNode.next = temp
        return head
#-----------------------------------------------------------------------------------------------------------------
#EXTRA POSSIBLE FUNCTIONS
    #FIND TASK WITH MAX DURATION
    def find_max_duration(self):

        if self.head is None:
            return None

        max_node = self.head
        current = self.head.next

        while current is not None:
            if current.duration > max_node.duration:
                max_node = current
            current = current.next

        return max_node

    #MERGE 2 TASK LISTS, SORTED BY PRIORITY
    def merge_with(self, other_list):

        merged = FactoryProduction()

        p1 = self.head
        p2 = other_list.head

        # Merge like in merge sort
        while p1 is not None and p2 is not None:
            if p1.priority <= p2.priority:
                merged.add_task(p1.task_name, p1.duration, p1.priority)
                p1 = p1.next
            else:
                merged.add_task(p2.task_name, p2.duration, p2.priority)
                p2 = p2.next

        # Remaining nodes from self
        while p1 is not None:
            merged.add_task(p1.task_name, p1.duration, p1.priority)
            p1 = p1.next

        # Remaining nodes from other_list
        while p2 is not None:
            merged.add_task(p2.task_name, p2.duration, p2.priority)
            p2 = p2.next

        return merged

    #REMOVE DUPLICATE TASKS
    def remove_duplicates(self):
        seen_names = set()
        current = self.head

        while current is not None:
            next_node = current.next  # store next before we possibly delete

            if current.task_name in seen_names:
                # Remove current node from the list

                # Case 1: current is head
                if current == self.head:
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                    else:
                        # list became empty
                        self.tail = None

                # Case 2: current is tail
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail is not None:
                        self.tail.next = None
                    else:
                        # list became empty
                        self.head = None

                # Case 3: middle node
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self.size -= 1

            else:
                # first time we see this name
                seen_names.add(current.task_name)

            current = next_node
