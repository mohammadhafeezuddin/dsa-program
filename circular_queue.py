class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        if self.isFull():
            print("Queue is Full")
            return
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(value, "inserted")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        value = self.queue[self.front]
        print(value, "deleted")
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Front element", self.queue[self.front])

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        print("Queue Elements:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


# Create circular queue
q = CircularQueue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.peek()
q.dequeue()
q.display()
q.enqueue(40)
q.enqueue(50)
q.display()
print("Is Queue Full:", q.isFull())
print("Is Queue Empty:", q.isEmpty())
