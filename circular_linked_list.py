class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new = Node(data)
        if self.head is None:
            new.next = new
            self.head = new
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        new.next = self.head
        temp.next = new
        self.head = new

    def insert_end(self, data):
        new = Node(data)
        if self.head is None:
            new.next = new
            self.head = new
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new
        new.next = self.head

    def insert_position(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return
        if pos == 1:
            self.insert_beginning(data)
            return
        if self.head is None:
            print("Invalid position")
            return
        temp = self.head
        for _ in range(pos - 2):
            temp = temp.next
            if temp == self.head:
                print("Invalid position")
                return
        new = Node(data)
        new.next = temp.next
        temp.next = new

    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        print(self.head.data, "deleted")
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        self.head = self.head.next
        temp.next = self.head

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            print(self.head.data, "deleted")
            self.head = None
            return
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        print(temp.next.data, "deleted")
        temp.next = self.head

    def delete_position(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos < 1:
            print("Invalid position")
            return
        if pos == 1:
            self.delete_beginning()
            return
        temp = self.head
        for _ in range(pos - 2):
            temp = temp.next
            if temp.next == self.head:
                print("Invalid position")
                return
        if temp.next == self.head:
            print("Invalid position")
            return
        print(temp.next.data, "deleted")
        temp.next = temp.next.next

    def search(self, key):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        pos = 1
        while True:
            if temp.data == key:
                print(key, "found at position", pos)
                return
            temp = temp.next
            pos += 1
            if temp == self.head:
                break
        print(key, "not found")

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)", self.head.data)


# Create an empty circular singly linked list
cll = CircularLinkedList()

cll.insert_beginning(20)
cll.insert_beginning(10)
cll.insert_end(40)
cll.insert_position(30, 3)
print("After insertion:")
cll.traverse()

cll.search(30)
cll.search(99)

cll.delete_beginning()
print("After deleting from beginning:")
cll.traverse()

cll.delete_end()
print("After deleting from end:")
cll.traverse()

cll.insert_end(50)
cll.insert_end(60)
cll.delete_position(2)
print("After deleting position 2:")
cll.traverse()
