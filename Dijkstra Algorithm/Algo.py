def dijkstra(graph, start):
    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    while True:
        currentNode = None
        smallestDistance = float('inf')
        for node in graph:
            if node not in visited and distances[node] < smallestDistance:
                currentNode = node
                smallestDistance = distances[node]
        if currentNode is None or smallestDistance == float('inf'):
            break
        visited.add(currentNode)

        for neighbor, weight in graph[currentNode].items():
            if neighbor not in visited:
                newDistance = distances[currentNode] + weight
                if newDistance < distances[neighbor]:
                    distances[neighbor] = newDistance
    return distances


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

print(f"Shortest distances from node {start_node}:")
for node, distance in shortest_distances.items():
    print(f"To node {node}: {distance}")


