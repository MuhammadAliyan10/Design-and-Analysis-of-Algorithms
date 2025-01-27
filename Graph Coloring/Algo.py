def graphColoring(graph):
    numVertices = len(graph)
    color = [-1] * numVertices
    color[0] = 0
    available = [False] * numVertices
    for u in range(1, numVertices):
        for v in range(numVertices):
            if graph[u][v] == 1 and color[v] != -1:
                available[color[v]] = True
        for c in range(numVertices):
            if not available[c]:
                color[u] = c
                break
        available = [False] * numVertices
    return color


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    colors = graphColoring(graph)
    print("Assigned Colors:", colors)
