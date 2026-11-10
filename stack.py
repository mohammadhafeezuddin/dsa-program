MAX = 5
stack = []
top = -1


def is_empty():
    return top == -1


def is_full():
    return top == MAX - 1


def push(value):
    global top
    if is_full():
        print("Stack Overflow: stack is full")
    else:
        stack.append(value)
        top = top + 1
        print(value, "pushed into stack")


def pop():
    global top
    if is_empty():
        print("Stack Underflow: stack is empty")
    else:
        value = stack.pop()
        top = top - 1
        print(value, "popped from stack")


def peek():
    if is_empty():
        print("Stack is empty")
    else:
        print("Top element is:", stack[top])


def display():
    if is_empty():
        print("Stack is empty")
    else:
        print("Stack elements are:")
        for i in range(top, -1, -1):
            print(stack[i])


print("Is stack empty:", is_empty())
push(10)
push(20)
push(30)
display()
peek()
pop()
display()
print("Is stack full:", is_full())
print("Is stack empty:", is_empty())
