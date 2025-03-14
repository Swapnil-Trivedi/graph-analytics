class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def bellman_ford(self, source):
        # Step 1: Initialize distances
        distance = {i: float('inf') for i in range(self.V)}
        distance[source] = 0

        print("Initial distances:", distance)

        # Step 2: Relax all edges (V-1) times
        for i in range(self.V - 1):
            print(f"\nIteration {i + 1}:")
            relaxed = False
            for u, v, w in self.edges:
                if distance[u] != float('inf') and distance[u] + w < distance[v]:
                    print(f"Relaxing edge ({u} -> {v}) with weight {w} | {distance[v]} -> {distance[u] + w}")
                    distance[v] = distance[u] + w
                    relaxed = True
                else:
                    print(f"Edge ({u} -> {v}) with weight {w} remains tense")
            
            if not relaxed:
                print("No changes in this iteration, stopping early.")
                break

        # Step 3: Check for negative-weight cycles
        print("\nChecking for negative-weight cycles:")
        for u, v, w in self.edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                print(f"Negative weight cycle detected via edge ({u} -> {v})")
                return

        print("\nNo negative weight cycles detected.")
        print("Final shortest distances from source:", distance)


def load_graph_from_file(filename):
    with open(file=filename, mode= 'r') as f:
        lines = f.readlines()

    edges = [tuple(map(int, line.strip().split())) for line in lines]
    vertices = max(max(u, v) for u, v, _ in edges) + 1

    g = Graph(vertices)
    for u, v, w in edges:
        g.add_edge(u, v, w)

    return g

if __name__ == '__main__':
    filename = "./weighted-digraph.txt"
    source = int(input("Enter the source vertex: ").strip())

    graph = load_graph_from_file(filename)
    graph.bellman_ford(source)
