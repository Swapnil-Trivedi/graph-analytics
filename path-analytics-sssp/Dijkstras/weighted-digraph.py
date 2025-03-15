import heapq

def dijkstra(graph_file, source):
    # Read graph from file
    graph = {}
    with open(graph_file, 'r') as f:
        for line in f:
            u, v, w = map(int, line.split())  # Read edge u -> v with weight w
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))

    # Initialize distances
    INF = float('inf')
    distances = {node: INF for node in graph}
    distances[source] = 0

    # Priority queue (min-heap)
    pq = [(0, source)]  # (distance, node)

    while pq:
        current_distance, u = heapq.heappop(pq)

        if current_distance > distances[u]:
            continue  # Skip outdated entries

        for v, weight in graph.get(u, []):
            if distances[u] + weight < distances[v]:  # Relaxation step
                distances[v] = distances[u] + weight
                heapq.heappush(pq, (distances[v], v))

    # Print final distances
    for node, dist in distances.items():
        print(f"Shortest path to {node}: {dist}")

# Example usage
dijkstra("weighted-digraph.txt", 1)
