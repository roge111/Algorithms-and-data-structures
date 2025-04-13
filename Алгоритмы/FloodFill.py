def app(coor, stack, seen):
    if coor not in seen:
                seen.add(coor)
                stack.append(coor)


def bfs(start, image, color):
    stack = [start]
    seen = {start}

    color_begin = image[start[0]][start[1]]
    
    while stack:
        
        i, j = stack.pop()
        image[i][j] = color
        

        if i > 0 and image[i-1][j] == color_begin:
            app((i-1, j), stack, seen)


        if i < len(image) - 1 and image[i + 1][j] == color_begin:
            app( (i+1, j), stack, seen)

        if j > 0 and image[i][j - 1] == color_begin:
            app( (i, j - 1), stack, seen)
        
        if j < len(image[i]) - 1 and image[i][j + 1] == color_begin:
            app((i, j+1), stack, seen)
    # return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1; sc = 1; color = 2
bfs((sr, sc), image, color)
print(image)

        