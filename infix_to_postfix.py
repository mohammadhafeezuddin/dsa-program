def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    postfix = ""
    for ch in expression:
        if ch.isalnum():
            postfix += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # remove '('
        else:
            while stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(ch):
                postfix += stack.pop()
            stack.append(ch)

    while stack:
        postfix += stack.pop()
    return postfix


expression = "A+B*C"
print("Infix expression:", expression)
print("Postfix expression:", infix_to_postfix(expression))
