def notRep(s: str) -> int:
    hash = {}
    l = 0
    max_len = 0

    for index, sym in enumerate(s):
        if sym in hash and hash[sym] >= l:
            l = hash[sym] + 1
        
        hash[sym] = index

        max_len = max(max_len, index - l + 1)

    return max_len

print(notRep('abcabcbb'))