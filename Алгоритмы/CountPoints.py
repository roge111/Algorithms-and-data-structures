def dfs(strings, start, n):
    stack = [start]
    seen = {start}
    count_points = 1

    while stack:
        row, column = stack.pop()

        

        if  strings[row][column + 1] == '.'and (row, column + 1) not in seen:
            stack.append((row, column + 1))
            seen.add((row, column + 1))
            count_points += 1
        
        if strings[row][column - 1] == '.'and (row, column - 1) not in seen:
            stack.append((row, column - 1))
            seen.add((row, column - 1))
            count_points += 1

        if strings[row + 1][column] == '.'and (row + 1, column) not in seen:
            stack.append((row + 1, column))
            seen.add((row + 1, column))
            count_points += 1
        
        if strings[row - 1][column] == '.' and (row - 1, column) not in seen:
            stack.append((row-1,column))
            seen.add((row - 1, column))
            count_points += 1
    return count_points

N = int(input())
strings = []
for i in range(N):
    strings.append(input())
start_row, start_column = input().split()
start_point = (int(start_row) - 1, int(start_column) - 1)

print(dfs(strings, start_point, N))