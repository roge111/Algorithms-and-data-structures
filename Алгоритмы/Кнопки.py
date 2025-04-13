def combination(digits: str) -> list:
    result = []

    hash = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7':'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    def rec(string, i):
        if len(digits) == len(string):
            result.append(string)
            return
        for ch in hash[digits[i]]:
            rec(string + ch, i+1)
    
    rec('', 0)
    return result

print(combination('23'))

        

