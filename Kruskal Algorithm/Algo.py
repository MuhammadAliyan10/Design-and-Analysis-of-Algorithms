class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def addEdge(self, src, dest, weight):
        self.edges.append(Edge(src, dest, weight))

    def findEdge(self, parent, i):
        if parent[i] != i:
            parent[i] = self.findEdge(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        xRoot = self.findEdge(parent, x)
        yRoot = self.findEdge(parent, y)
        if rank[xRoot] < rank[yRoot]:
            parent[xRoot] = yRoot
        elif rank[xRoot] > rank[yRoot]:
            parent[yRoot] = xRoot
        else:
            parent[yRoot] = xRoot
            rank[xRoot] += 1

    def kruskal(self):
        result = []
        self.edges.sort(key=lambda x: x.weight)
        parent = list(range(self.vertices))
        rank = [0] * self.vertices
        e = 0
        i = 0
        while e < self.vertices - 1:
            edge = self.edges[i]
            i += 1
            x = self.findEdge(parent, edge.src)
            y = self.findEdge(parent, edge.dest)
            if x != y:
                e += 1
                result.append(edge)
                self.union(parent, rank, x, y)
        return result


if __name__ == "__main__":
    graph = Graph(4)
    graph.addEdge(0, 1, 10)
    graph.addEdge(0, 2, 6)
    graph.addEdge(0, 3, 5)
    graph.addEdge(1, 3, 15)
    graph.addEdge(2, 3, 4)
    mst = graph.kruskal()
    for edge in mst:
        print(f"{edge.src} -- {edge.dest} == {edge.weight}")
