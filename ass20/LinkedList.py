from Node import Node

class LinkedList:
    def __init__(self, value=None):
        if value is not None:
            self.head = Node(value)
        else:
            self.head = None
        self.tail = self.head

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self):
        if self.head is None:
            print("List is empty. Cannot remove from an empty list.")
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
