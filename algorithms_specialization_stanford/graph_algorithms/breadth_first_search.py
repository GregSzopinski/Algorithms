from queue import Queue
from graph_utils import example_graph_823


example_graph = example_graph_823()


# Initialize q with s
def bfs(graph, starting_vertex):
    """
    Basic implementation of breadth-first search algorithm.
    I try to keep the same names as in the book - check example 8.2.3 for reference.
    This implementation also features more printing to show step by step what is going on.
    """
    explored = [starting_vertex]
    q = Queue()
    q.put(starting_vertex)

    while not q.empty():
        v = q.get()
        print(f"current vertex: {v}")
        for w in graph.adj_list[v]:
            print(f"current edge: {v, w}")
            if w not in explored:
                explored.append(w)
                q.put(w)
            else:
                print(f"Vertex {w} is already explored")


def main():
    bfs(example_graph, "s")


if __name__ == '__main__':
    main()


