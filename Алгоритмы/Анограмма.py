def isAnagram(s, t):    
    if len(s) != len(t):
        return False

    hash = {}
    for i in s:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1

    for i in t:
        if i in hash:
            if hash[i] > 0:
                hash[i] -= 1
            else:
                return False
        else:
            return False
    return True

print(isAnagram("anagram", "nagaram"))