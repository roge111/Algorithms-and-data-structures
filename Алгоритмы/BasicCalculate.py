def basciCalculate(str):
    stack = []
    num = 0
    result = 0
    sign = 1

    for symbol in str:
        if symbol.isdigit():
            num += num * 10 + int(symbol)
        elif symbol == '+':
            result += sign * num
            num  = 0
            sign = 1
        elif symbol == '-':
            result += sign * num
            num = 0
            sign = -1
        elif symbol == '(':
            stack.append((result, sign))
            result = 0
            sign = 1
        elif symbol == ')':

            result += sign * num
            last_result, last_sign = stack.pop()
            result = last_result + last_sign * result
    result += sign * num
    return result
            
        
