def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    hash_map = {}
    for point in points:
        key = ((point[0] - 0)**2 + (point[1] - 0)**2)**0.5
        if key in hash_map:
            hash_map[key].append(point)
        else:
            hash_map[key] = [point]
    keys_sort = sorted(hash_map)
    
    result = []
    
    cnt = 0
    for i, key in enumerate(keys_sort):
        for point in hash_map[key]:
            result.append(point)
            cnt +=1
        if cnt == k:
            return result
print(kClosest([[0,1],[1,0]], 2))

# [[0,1],[1,0]]
# 2