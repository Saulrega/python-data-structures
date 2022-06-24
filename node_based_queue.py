"""
Code used during the class 'Queues basadas en nodos'.
"""
from double_node import TwoWayNode


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = TwoWayNode(data, None, None)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def dequeue(self):
        current = self.head

        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1

        return current.data


"""
Code used in the shell

x = Queue()

x.enqueue('eggs')
x.enqueue('ham')
x.enqueue('spam')
x.head.data
x.head.next.data
x.tail.data
x.count
x.dequeue()
x.head
"""