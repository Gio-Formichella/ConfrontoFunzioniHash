from node import *


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item):  # returns if item is found or not and number of inspected items
        current = self.head
        found = False
        inspected = 0  # number of examined items
        while current is not None and not found:
            inspected += 1
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found, inspected

    def remove(self, item):  # also returns number of inspected elements
        current = self.head
        previous = None
        found = False
        inspected = 0
        while not found and current is not None:
            inspected += 1
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if found:
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

        return found, inspected
