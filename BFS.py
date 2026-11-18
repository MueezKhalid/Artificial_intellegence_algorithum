from collections import deque

graph = {
    'S': [('A', 3), ('C', 2), ('D', 2)],
    'A': [],
    'B': [('E', 2)],
    'C': [('F', 1)],
    'D': [('B', 3), ('G', 8)],
    'E': [('G', 2)],
    'F': [('E', 0), ('G', 4)],
    'G': []
}


def bfs(start, goal):
    queue = deque([(start, [start], 0)])
    explored = []

    while queue:
        node, path, cost = queue.popleft()

        if node in explored:
            continue
        explored.append(node)

        if node == goal:
            return explored, path, cost

        for neighbour, weight in sorted(graph[node]):
            if neighbour not in explored:
                queue.append((neighbour, path + [neighbour], cost + weight))

    return explored, None, 0


explored, path, cost = bfs('S', 'G')

print("Explored:", explored)
print("Path:", " -> ".join(path))
print("Cost:", cost)