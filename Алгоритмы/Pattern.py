def patternWord(pattern: str, s: str) -> bool:
    string = s.split()
    hash_word = {}
    hash_pattern = {}

    for index, el in enumerate(pattern):
        if string[index] in hash_word:
            if hash_word[string[index]] != el:
                return False
        else:
            if el not in hash_pattern:
                hash_word[string[index]] = el
                hash_pattern[el] = string[index]
            else:
                return False
        
    return True

print(patternWord('abba', 'dog cat cat dog'))