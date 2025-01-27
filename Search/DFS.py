class GraphDFS:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {i: [] for i in range(vertices)}

    def addEdge(self, src, dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def dfsUtil(self, vertex, visited, result):
        visited[vertex] = True
        result.append(vertex)
        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                self.dfsUtil(neighbor, visited, result)

    def dfs(self, start):
        visited = [False] * self.vertices
        result = []
        self.dfsUtil(start, visited, result)
        return result


if __name__ == "__main__":
    graph = GraphDFS(6)
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 4)
    graph.addEdge(3, 5)

    print("DFS starting from vertex 0:", graph.dfs(0))
