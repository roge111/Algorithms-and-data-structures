def generate(numRows):
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    triangle = [[1], [1, 1], [1, 2, 1]]
    i = 3
    while len(triangle) < numRows:
        row = [1]
        j = 1
        last_row = triangle[i-1]
        while j < len(last_row):
            row.append(last_row[j-1] + last_row[j])
            j += 1
        row.append(1)

        triangle.append(row)
        i += 1
    return triangle


print(generate(3))