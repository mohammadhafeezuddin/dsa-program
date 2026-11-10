class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new = Node(data)
        if self.head is not None:
            new.next = self.head
            self.head.prev = new
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
        new.prev = temp

    def insert_position(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return
        if pos == 1:
            self.insert_beginning(data)
            return
        temp = self.head
        for _ in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next
        if temp is None:
            print("Invalid position")
            return
        new = Node(data)
        new.next = temp.next
        new.prev = temp
        if temp.next is not None:
            temp.next.prev = new
        temp.next = new

    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        print(self.head.data, "deleted")
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            print(self.head.data, "deleted")
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        print(temp.data, "deleted")
        temp.prev.next = None

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
        for _ in range(pos - 1):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next
        if temp is None:
            print("Invalid position")
            return
        print(temp.data, "deleted")
        temp.prev.next = temp.next
        if temp.next is not None:
            temp.next.prev = temp.prev

    def search(self, key):
        temp = self.head
        pos = 1
        while temp:
            if temp.data == key:
                print(key, "found at position", pos)
                return
            temp = temp.next
            pos += 1
        print(key, "not found")

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        print("Forward: None <-> ", end="")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def traverse_reverse(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        print("Reverse: None <-> ", end="")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


# Create an empty doubly linked list
dll = DoublyLinkedList()

dll.insert_beginning(20)
dll.insert_beginning(10)
dll.insert_end(40)
dll.insert_position(30, 3)
print("After insertion:")
dll.traverse()
dll.traverse_reverse()

dll.search(30)
dll.search(99)

dll.delete_beginning()
print("After deleting from beginning:")
dll.traverse()

dll.delete_end()
print("After deleting from end:")
dll.traverse()

dll.insert_end(50)
dll.insert_end(60)
dll.delete_position(2)
print("After deleting position 2:")
dll.traverse()
dll.traverse_reverse()
