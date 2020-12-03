from queue import Queue
from graph_utils import Graph, example_graph_823


example_graph = example_graph_823()
# todo: BFS implementation
# Initialize q with s
starting_vertex = example_graph.vertices[0]
explored = [starting_vertex]
q = Queue()
q.put(starting_vertex)

while not q.empty():
    v = q.get()
    print(f"current vertex: {v}")
    for endpoint in example_graph.adj_list[v]:
        print(f"current edge: {v, endpoint}")
        if endpoint not in explored:
            explored.append(endpoint)
            q.put(endpoint)
        else:
            print(f"Vertex {endpoint} is already explored")
