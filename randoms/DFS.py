class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        self._dfs_util(start, visited, 0)

    def _dfs_util(self, vertex, visited, depth):
        visited.add(vertex)
        print("  " * depth + vertex)

        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    self._dfs_util(neighbor, visited, depth + 1)


# Example usage
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')

print("Depth-First Traversal (DFS):")
graph.dfs('C')
