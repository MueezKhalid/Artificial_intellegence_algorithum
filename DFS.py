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


def dfs(start, goal):
    stack = [(start, [start], 0)]
    explored = []

    while stack:
        node, path, cost = stack.pop()

        if node in explored:
            continue
        explored.append(node)

        if node == goal:
            return explored, path, cost

        for neighbour, weight in reversed(sorted(graph[node])):
            if neighbour not in explored:
                stack.append((neighbour, path + [neighbour], cost + weight))

    return explored, None, 0


explored, path, cost = dfs('S', 'G')

print("Explored:", explored)
print("Path:", " -> ".join(path))
print("Cost:", cost)