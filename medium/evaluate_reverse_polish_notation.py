
tokens = ["1","2","+","3","*","4","-"]

def evalRPN(tokens):
    stack = []

    for character in tokens:
        if character == "+":
            stack.append(stack.pop() + stack.pop())
        elif character == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif character == "*":
            stack.append(stack.pop() * stack.pop())
        elif character == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b/a))
        else:
            stack.append(int(character))
    return stack[0]

if __name__ == "__main__":
    print(evalRPN(tokens))