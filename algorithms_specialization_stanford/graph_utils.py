class Graph:
    def __init__(self, vertices, directed=False):
        self.vertices = vertices
        self.directed = directed
        self.adj_list = {}

        for vertex in self.vertices:
            self.adj_list[vertex] = []

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        if not self.directed:
            self.adj_list[v].append(u)

    def degree(self, vertex):
        print(len(self.adj_list[vertex]))

    def print_adj_list(self):
        for vertex in self.vertices:
            print(vertex, "->", self.adj_list[vertex])


def example_graph() -> object:
    """Create example, hard-coded graph and print its attributes"""

    vertices = ["A", "B", "C", "D", "E"]
    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("C", "E"),
        ("D", "E"),
    ]

    graph = Graph(vertices)
    for u, v in edges:
        graph.add_edge(u, v)
    graph.print_adj_list()
    graph.degree("A")
