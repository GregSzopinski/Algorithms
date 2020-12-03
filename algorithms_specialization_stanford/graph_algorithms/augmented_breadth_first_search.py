from queue import Queue
from graph_utils import Graph, example_graph_823

# Example 8.2.3 from Algorithms Illuminated Part 2 - undirected graph with six vertices
example_graph = example_graph_823()


def augmented_bfs(graph, starting_vertex):
    """
    Augmented version of breadth-first search algorithm, able to find shortest paths from starting vertex.
    Shortest path here means here number of 'hops' from given vertex.
    """
    explored = [starting_vertex]
    # shortest paths as number of 'hops' form starting vertex
    shortest_paths = {
        vertex: 0 if vertex == starting_vertex else float("inf")
        for vertex in graph.vertices
    }
    q = Queue()
    q.put(starting_vertex)

    while not q.empty():
        v = q.get()
        for endpoint in graph.adj_list[v]:
            if endpoint not in explored:
                explored.append(endpoint)
                shortest_paths[endpoint] = shortest_paths[v] + 1
                q.put(endpoint)

    return shortest_paths


def main():
    print(augmented_bfs(example_graph, "s"))


if __name__ == "__main__":
    main()
