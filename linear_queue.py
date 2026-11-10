class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if self.isFull():
            print("Queue is Full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = value
            print(value, "inserted in queue")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            value = self.queue[self.front]
            print(value, "removed from queue")
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front += 1

    def front_element(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Front element is", self.queue[self.front])

    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue elements:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

    def isFull(self):
        return self.rear == self.size - 1

    def isEmpty(self):
        return self.front == -1


q = Queue(5)
print("Is queue empty:", q.isEmpty())
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.front_element()
q.dequeue()
q.display()

if q.isFull():
    print("Queue is Full")
else:
    print("Queue is Not Full")
