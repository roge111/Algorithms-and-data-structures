def bfs(start, grid):
    stack = [start]
    seen = {start}
    p = 0
    while stack:
        cur = stack.pop()
        i, j = cur[0], cur[1]
        
        #Проверка на то, что клетка на границе сверху или снизу или справа или слева
        if i == 0:
            p += 1
        if i == len(grid) - 1:
            p += 1
        if j == len(grid[i]) - 1:
            p += 1
        if j == 0:
            p += 1
        
        #Проверка клетки сверху на 0 или 1, если это не граница. Если 1, то добавляем в стек, если ее не смотрели
        if i > 0 and grid[i-1][j] == 0:
            p += 1
        elif i > 0:
            if (i - 1, j) not in seen:
                stack.append((i - 1, j))
                seen.add((i - 1, j))

        #Проверка клетки снизу на 0 или 1, если это не граница. Если 1, то добавляем в стек, если ее не смотрели
        if i < len(grid) - 1 and grid[i + 1][j] == 0:
            p += 1
        elif i < len(grid) - 1:
            if (i + 1, j) not in seen:
                stack.append((i + 1, j))
                seen.add((i + 1, j))



        #Проверка клетки слева на 0 или 1, если это не граница поля. Если 1, то добавляем в стек, если ее не смотрели
        if j > 0 and grid[i][j - 1] == 0:
            p += 1
        elif j > 0:
            if (i, j - 1) not in seen:
                stack.append((i, j - 1))
                seen.add((i, j - 1))

        #Проверка клетки справа на 0 или 1, если это не граница поля. Если 1, то добавляем в стек, если ее не смотрели
        if j < len(grid[i]) - 1 and grid[i][j + 1] == 0:
            p += 1
        elif j < len(grid[i]) - 1:
            if (i, j + 1) not in seen:
                stack.append((i, j + 1))
                seen.add((i, j + 1))

    return p

grid = [[1, 0]]
start = (0, 0)

for i in range(len(grid)):
    f = False
    for j in range(len(grid[i])):
        if grid[i][j] == 1:
            start = (i, j)
            f = True
            break
    if f:
        break



print(bfs(start, grid))