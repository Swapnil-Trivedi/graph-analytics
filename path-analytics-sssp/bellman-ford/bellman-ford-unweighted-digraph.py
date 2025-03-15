from collections import defaultdict

def read_graph(filename):
    graph = defaultdict(list)
    with open(filename, 'r') as f:
        for line in f:
            u, v = map(int, line.strip().split())
            graph[u].append((v, 1))  # Treat every edge with weight = 1
            if v not in graph:
                graph[v] = []
    return graph

def bellman_ford(graph, source):
    # Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    V = len(graph)

    print("Starting Bellman-Ford for unweighted graph...")

    # Relax edges (V-1) times
    for i in range(V - 1):
        print(f"Iteration {i + 1}:")
        updated = False

        for u in graph:
            for v, w in graph[u]:
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    updated = True
                    print(f"Relaxing edge ({u} -> {v}): New distance to {v} = {distances[v]}")

        if not updated:
            print("No updates in this iteration. Early exit.")
            break

    # Detect negative weight cycles
    print("Checking for negative weight cycles...")
    for u in graph:
        for v, w in graph[u]:
            if distances[u] + w < distances[v]:
                print("Negative weight cycle detected!")
                return None

    return distances

def main():
    filename = "./unweighted-digraph.txt"
    source = int(input("Enter the source vertex: ").strip())

    graph = read_graph(filename)

    if source not in graph:
        print("Error: Source vertex not found in graph.")
        return

    distances = bellman_ford(graph, source)

    if distances:
        print("\nFinal shortest distances from source:")
        for node, dist in sorted(distances.items()):
            print(f"Node {node}: Distance {dist}")

if __name__ == '__main__':
    main()
