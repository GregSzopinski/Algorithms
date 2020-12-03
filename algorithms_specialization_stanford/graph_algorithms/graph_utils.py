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


def example_graph_823():
    # Example 8.2.3 from Algorithms Illuminated Part 2 - undirected graph with six vertices
    example_graph = Graph(["s", "a", "b", "c", "d", "e"])
    example_graph.add_edge("s", "a")
    example_graph.add_edge("s", "b")
    example_graph.add_edge("a", "c")
    example_graph.add_edge("b", "c")
    example_graph.add_edge("c", "d")
    example_graph.add_edge("c", "e")
    example_graph.add_edge("d", "e")
    return example_graph