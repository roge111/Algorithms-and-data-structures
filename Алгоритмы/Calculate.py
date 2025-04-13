def calculate(s: str) -> int:
    stack = []
    num = 0
    operation = '+'


    for index, sym in enumerate(s):
        if sym.isdigit():
            num  = num * 10 + int(sym)
        if (not(sym.isdigit()) and sym != ' ') or index == len(s) - 1:
            if operation == '+':
                stack.append(num)
            elif operation == '-':
                stack.append(-num)
            elif operation == '*':
                stack.append(stack.pop() * num)
            else:
                dig = stack.pop()
                if dig // num < 0 and dig % num != 0:
                    stack.append(dig // num + 1)
                else:
                    stack.append(dig//num)
            num = 0
            operation = sym
    return sum(stack)
s = input("Введите выражение: ")
print(calculate(s))