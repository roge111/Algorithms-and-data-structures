def groupAnagrams(strs: str) -> list:
    hash = {}
    
    for word in strs:
        word_s = ''.join(sorted(word))
        if word_s in hash:
            hash[word_s].append(word)
        else:
            hash[word_s] = [word]
    
    result = []
    for key in hash:
        result.append(hash[key])
    return result
print(groupAnagrams(["a"]))