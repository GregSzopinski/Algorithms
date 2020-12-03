from queue import Queue
from graph_utils import Graph

# Example 8.2.3 from Algorithms Illuminated Part 2 - undirected graph with six vertices
example_graph = Graph(['s', 'a', 'b', 'c', 'd', 'e'])

example_graph.add_edge('s', 'a')
example_graph.add_edge('s', 'b')
example_graph.add_edge('a', 'c')
example_graph.add_edge('b', 'c')
example_graph.add_edge('c', 'd')
example_graph.add_edge('c', 'e')
example_graph.add_edge('d', 'e')

# todo: BFS implementation
# Initialize q with s
explored = [example_graph.vertices[0]]
q = Queue()
q.put(example_graph.vertices[0])

while not q.empty():
    v = q.get()
    print(f"current vertex: {v}")
    for endpoint in example_graph.adj_list[v]:
        print(f"current edge: {v, endpoint}")
        if endpoint not in explored:
            explored.append(endpoint)
            q.put(endpoint)


