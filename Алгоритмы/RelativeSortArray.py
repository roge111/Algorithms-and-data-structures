

def relativeSortArray(arr1: list, arr2: list ) -> list:
    hash = {}
    data = {}

    for i in range(len(arr1)):
        el = arr1.pop()
        if el in arr2:
            ind = arr2.index(el)
            if ind not in hash:
                hash[ind] = [el]
            else:
                hash[ind].append(el)
        else:
            if len(data) == 0:
                data = {el}
            else:
                data.add(el)
    keys = sorted(hash)
    result = []

    for key in keys:
        for el in hash[key]:
            result.append(el)
    for el in data:
        result.append(el)
    return result

print(relativeSortArray([2, 2, 19, 1, 6, 3, 4], [2, 1, 3, 6]))
    
