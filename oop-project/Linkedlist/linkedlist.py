class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Node | None = None

class LinkedList:
    def __init__(self):
        self.head: Node | None = None
    # add a new node
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # add a new node in a certain order
    def insert(self, prev_data, new_data):
        if prev_data is None:
            raise ValueError
        new_node = Node(new_data)
        new_node.next = prev_data.next
        prev_data.next = new_node

    # add a new node to the end of list
    def append (self, new_data):
        new_node = Node (new_data)
        if self.head is None:
            self.head = new_node
            return 
        
        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def printData(self):
        item = self.head
        while item:
            print(item.data)
            item = item.next

lis = LinkedList()

first = Node(1)
second = Node(2)
third = Node(3)

lis.head = first
lis.head.next = second
second.next = third

lis.push(0)
lis.insert(second,9)
lis.append(10)

lis.printData()
