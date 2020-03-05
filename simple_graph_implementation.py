from queue import Queue
class Graph:
    """ A simple class to implement a graph with vertices
    numbered 1 (or 0) to vertex_count"""
    vertex_count = 10000
    # an adjacency list to maintain our edges
    # for each vertex we will have a list where we keep
    # all vertices adjacent to it
    adj = []

    def __init__(self, vertices = 10000):
        # add 1 so we have no problems with indexing 
        # 1 to vertex_count 
        self.vertex_count = vertices + 1
        self.adj = [[] for i in range(self.vertex_count)]

    def add_edge(self, u, v):
        """ adds a bidirectional edge between u and v"""
        self.adj[u].append(v)
        self.adj[v].append(u)

    # a list which we will use while performing our searches
    # (traversals) so we don't create a perpetual loop
    visited = []

    # depth-first search (traversal)
    def dfs(self, v):
        print(f"Current vertex: {v}")
        self.visited[v] = True
        for u in self.adj[v]:
            if not self.visited[u]:
                self.dfs(u)

    def do_dfs(self, source = 1):
        print()
        print("Performing dfs")
        self.visited = [False] * self.vertex_count
        self.dfs(source)
        print()

    # breadth-first search (traversal)
    def bfs(self, source):
        q = Queue(self.vertex_count)
        q.put(source)
        self.visited[source] = True
        while not q.empty():
            v = q.get()
            print(f"Current vertex {v}")
            for u in self.adj[v]:
                if not self.visited[u]:
                    q.put(u)
                    self.visited[u] = True

    def do_bfs(self, source = 1):
        print()
        print("Performing bfs")
        self.visited = [False] * self.vertex_count
        self.bfs(source)
        print()

g = Graph(10)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(4, 7)
g.do_dfs(1)
g.do_bfs(1)
