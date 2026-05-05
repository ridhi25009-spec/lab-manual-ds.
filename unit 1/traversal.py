from collections import deque

def bfs_shortest_path(graph, start, end):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(path + [neighbor])

    return "No path"


def dfs_depth(graph, start, depth):
    result = set()

    def dfs(node, d):
        if d > depth:
            return
        result.add(node)

        for neighbor in graph[node]:
            if neighbor not in result:
                dfs(neighbor, d + 1)

    dfs(start, 0)
    result.discard(start)
    return result