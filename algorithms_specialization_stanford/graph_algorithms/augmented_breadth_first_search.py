from queue import Queue
from graph_utils import Graph, example_graph_823

# Example 8.2.3 from Algorithms Illuminated Part 2 - undirected graph with six vertices
example_graph = example_graph_823()

# Initialize q with s
starting_vertex = example_graph.vertices[0]
explored = [starting_vertex]
# shortest paths as number of 'hops' form starting vertex
shortest_paths = {vertex: 0 if vertex == starting_vertex else float("inf") for vertex in example_graph.vertices}
q = Queue()
q.put(starting_vertex)

while not q.empty():
    v = q.get()
    print(f"current vertex: {v}")
    for endpoint in example_graph.adj_list[v]:
        print(f"current edge: {v, endpoint}")
        if endpoint not in explored:
            explored.append(endpoint)
            shortest_paths[endpoint] = shortest_paths[v] + 1  # shortest path part 2
            q.put(endpoint)
        else:
            print(f"Vertex {endpoint} is already explored")

print(shortest_paths)
