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
    queue_to_explore = Queue()
    queue_to_explore.put(starting_vertex)

    while not queue_to_explore.empty():
        v = queue_to_explore.get()
        for w in graph.adj_list[v]:
            if w not in explored:
                explored.append(w)
                shortest_paths[w] = shortest_paths[v] + 1
                queue_to_explore.put(w)

    return shortest_paths


def main():
    print(augmented_bfs(example_graph, "s"))


if __name__ == "__main__":
    main()
