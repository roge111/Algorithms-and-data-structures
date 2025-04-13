from collections import Counter

def frequency(s: str) -> str:
    count_char = Counter(s)

    sorted_chars = sorted(count_char.items(), key=lambda item: item[1], reverse=True)
    
    result = ''
    for cahrs in sorted_chars:
        result += cahrs[0]*cahrs[1]
    return result

print(frequency('Aabb'))


