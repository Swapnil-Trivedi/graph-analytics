# Dijkstra's Algorithm for Unweighted Directed Graphs (Handles Disconnected Components)

import heapq
from collections import defaultdict
import sys

def load_graph(filename):
    graph = defaultdict(list)
    vertices = set()

    with open(filename, 'r') as f:
        for line in f:
            u, v = map(int, line.strip().split())
            graph[u].append(v)
            vertices.update([u, v])

    return graph, vertices

def dijkstra_unweighted(graph, vertices, start):
    INF = float('inf')
    distances = {v: INF for v in vertices}
    distances[start] = 0

    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        # Explore neighbors
        for neighbor in graph.get(current_vertex, []):
            new_distance = current_distance + 1

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    return distances

if __name__ == "__main__":
    filename = "unweighted-digraph.txt"

    try:
        graph, vertices = load_graph(filename)
        start_node = int(input("Enter the source vertex: "))

        if start_node not in vertices:
            print("Source vertex not in graph.")
            sys.exit(1)

        distances = dijkstra_unweighted(graph, vertices, start_node)

        print("\nShortest distances from node", start_node, ":")
        for vertex in sorted(vertices):
            print(f"Node {vertex}: Distance {distances[vertex]}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: Invalid input. Ensure the graph file is properly formatted.")