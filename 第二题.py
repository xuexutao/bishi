def solve(s):
    stack = []
    index = []
    result = []

    for i, char in enumerate(s):
        if char == "(":
            stack.append(char)
            index.append(i)
        elif char == ")":
            if not stack:  # 栈空
                result.append('?')
            else:
                top = stack.pop()
                index.pop()
                if top == '(':
                    result.append(' ')
                    result.append(' ')
                else:
                    result.append('?')
        else:
            result.append(' ')

    for i in index:
        result.insert(i, 'x')

    return ''.join(result)


if __name__ == '__main__':
    inputs = [
        "bge)))))))))",
        "((IIII))))))",
        "()()()()(uuu",
        "))))UUUU((()"
    ]
    for inp in inputs:
        print(inp)
        print(solve(inp))
