def operStack(stack):
    result = 0
    for j in range(len(stack)):
        i = stack.pop()
        index = len(stack)

        if i < 0 and index == 0:
            result = -i
        elif i > 0 and index == 0:
            result = i
        elif index >  0:
            if i < 0:
                if -i:
                    i = 1
                else:
                    i = 0
                if result:
                    result = 1
                else:
                    result = 0
                result = result != i
            else:
                if i:
                    i = 1
                else:
                    i = 0
                if result:
                    result = 1
                else:
                    result = 0
                result = result or i
    return result

def logicCalculate(string):
    stack = []
    stack2 = []
    operation = '|'
    result = 0

    for sym in string:
        if sym.isdigit():
            num = int(sym)
        else:
            if operation == '|' and sym != '(':
                stack.append(num)
            elif operation == '&' and sym != '(':
                el = stack.pop()
                if el < 0:
                    stack.append(-el and num)
                else:
                    stack.append(el and num)
                
            elif operation == '^' and sym != '(':
                stack.append(-1)
            elif sym == '(':
                result = operStack(stack) #Результат до скобки вычисляется и сохранятеся
                stack2.append((result, operation))
            elif sym == ')':
                result = operation(stack)
                last_result, last_operation = stack2.pop()
                num = last_result
                if last_operation == '|':
                    stack.append(num)
                elif last_operation == '&':
                    el = stack.pop()
                    if el < 0:
                        stack.append(-el and num)
                    else:
                        stack.append(el and num)
                    
                elif last_operation == '^':
                    stack.append(-1)
            operation = sym
string = '1|(0&0^1)'
print(logicCalculate(string))

