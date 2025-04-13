def setZeroes(matrix):
    r = len(matrix)
    c= len(matrix[-1])

    rows = set()
    columns = set()
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                rows.add(i)
                columns.add(j)
    
    for i in range(r):
        for j in range(c):
            if i in rows or j in columns:
                matrix[i][j] = 0

matrix = [[1,1,0], [0,0,1], [1, 1, 1]]
setZeroes(matrix)
print(matrix)
