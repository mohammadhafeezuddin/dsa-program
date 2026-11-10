class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def insert_position(self, data, pos):
        if pos == 1:
            self.insert_beginning(data)
            return
        new = Node(data)
        temp = self.head
        for i in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next
        if temp is None:
            print("Invalid position")
            return
        new.next = temp.next
        temp.next = new

    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None

    def delete_position(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 1:
            self.head = self.head.next
            return
        temp = self.head
        for i in range(pos - 2):
            if temp.next is None:
                print("Invalid position")
                return
            temp = temp.next
        if temp.next is None:
            print("Invalid position")
            return
        temp.next = temp.next.next

    def search(self, key):
        temp = self.head
        pos = 1
        while temp:
            if temp.data == key:
                print(key, "found at", pos)
                return
            temp = temp.next
            pos += 1
        print(key, "not found")

    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")


l = LinkedList()

l.insert_beginning(20)
l.insert_beginning(10)
l.insert_end(40)
l.insert_position(30, 3)
print("After Insertion:")
l.display()

l.search(30)
l.delete_beginning()
print("After deleting from beginning:")
l.display()
l.delete_position(2)
print("After deleting position 2:")
l.display()
