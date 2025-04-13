def reverseStr(s: str, k: int) -> str:
    result = ''
    f = True
    for i in range(0, len(s), k):
        part = s[i:i+k]
        if f: 
            result += part[::-1]
            f = False
        else:
            result += part
            f = True
    return result
print(reverseStr('abcdefg', 2))
            