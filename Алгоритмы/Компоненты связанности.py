import sys

def dfs(graph, start):
    stack = [start]
    seen = {start}

    while stack:
        cur = stack.pop()
        if cur in graph:
            for point in graph[cur]:
                if point not in seen:
                    seen.add(point)
                    stack.append(point)
    return seen



def main():

    N, M = map(int, input().split())
    graph = {}
    points = {str(i) for i in range(1, N + 1)}

    for i in range(M):
        x, y = input().split()
        if x not in graph:

            graph[x] = [y]
        else:
            graph[x].append(y)

        if y not in graph:
            graph[y] = [x]
        else:
            graph[y].append(x)


    c = 0
    result = []
    seen_total = set()
    for v in points:
        if v not in seen_total:
            c += 1
            res = dfs(graph, v)
            
            result.append( (len(res), res))
        
    print(c)
    for el in result:
        cnt, res = el
        print(cnt)
        print(' '.join(list(res)))
    pass


if __name__ == '__main__':
    main()