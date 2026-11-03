
string = "([{])"

def isValid(string):

    stack = []
    closedToOpen = {"}": "{", "]": "[", ")":"("}

    for bracket in string:
        if bracket in closedToOpen:
            if stack and stack[-1] == closedToOpen[bracket]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)

    return not stack


if __name__ == "__main__":

    print(isValid(string))
