class GraphBFS:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {i: [] for i in range(vertices)}

    def addEdge(self, src, dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def bfs(self, start):
        visited = [False] * self.vertices
        queue = [start]
        visited[start] = True
        result = []
        while queue:
            vertex = queue.pop(0)
            result.append(vertex)
            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        return result


if __name__ == "__main__":
    graph = GraphBFS(6)
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 4)
    graph.addEdge(3, 5)

    print("BFS starting from vertex 0:", graph.bfs(0))
