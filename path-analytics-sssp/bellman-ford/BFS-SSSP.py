from collections import defaultdict, deque

def read_graph(filename):
    graph = defaultdict(set)
    all_nodes = set()

    with open(filename, 'r') as f:
        for line in f:
            u, v = map(int, line.strip().split())
            graph[u].add(v)
            all_nodes.update([u, v])

    # Ensure all nodes (even those only appearing as destinations) are included
    for node in all_nodes:
        if node not in graph:
            graph[node] = set()

    return graph

def bfs_shortest_path(graph, source):
    # Initialize distances and queue
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    queue = deque([source])

    print("Starting BFS from source:", source)

    # BFS traversal
    while queue:
        current = queue.popleft()

        print(f"Exploring node {current} with current distance {distances[current]}")

        for neighbor in graph[current]:
            # If a shorter path is found
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
                print(f"Relaxed: {neighbor}, New Distance: {distances[neighbor]}")

    return distances

def main():
    filename = "./unweighted-digraph.txt"
    source = int(input("Enter the source vertex: ").strip())

    graph = read_graph(filename)

    # Ensure the source exists in the graph
    if source not in graph:
        print("Error: Source vertex not found in graph.")
        return

    distances = bfs_shortest_path(graph, source)

    print("\nFinal shortest distances from source:")
    for node, dist in sorted(distances.items()):
        print(f"Node {node}: Distance {dist}")

if __name__ == '__main__':
    main()