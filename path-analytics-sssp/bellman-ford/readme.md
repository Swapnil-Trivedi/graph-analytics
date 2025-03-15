# Bellman-Ford Algorithm Implementation (Weighted & Unweighted Directed Graphs)

## 📌 Overview
This project implements the **Bellman-Ford algorithm** for both **weighted** and **unweighted** directed graphs. The algorithm computes the **shortest path** from a **single source vertex** to all other vertices. Additionally, it can detect the presence of **negative weight cycles** in the graph.

---

## 📂 Directory Structure

```
├── bellman_ford_weighted.py       # Bellman-Ford for weighted digraphs
├── bellman_ford_unweighted.py     # Bellman-Ford for unweighted digraphs
└── weighted-digraph.txt           # Input graph (user-provided)
```

---

## 📊 Bellman-Ford Algorithm

The **Bellman-Ford algorithm** works by iteratively relaxing all edges, updating the shortest path estimates. It can handle:
- **Negative weight edges**
- **Detection of negative weight cycles**
- **Disconnected components (infinite distances)**

### 🧮 Core Idea (Relaxation Process):
For each edge **(u, v)** with weight **w**:

If:  
\[ d[v] > d[u] + w \]  
Then:  
\[ d[v] = d[u] + w \]

This repeats for **V - 1** iterations (where **V** is the number of vertices), ensuring that the shortest path is computed.

---

## 📌 Input Format
The graph is provided via a **text file** where each line represents an edge.

### **Weighted Graph Input (bellman_ford_weighted.py)**
```
1 2 5  # Edge from vertex 1 to vertex 2 with weight 5
2 3 -2 # Edge from vertex 2 to vertex 3 with weight -2
3 1 4  # Edge from vertex 3 to vertex 1 with weight 4
```

### **Unweighted Graph Input (bellman_ford_unweighted.py)**
```
1 2    # Edge from vertex 1 to vertex 2 (weight assumed as 1)
2 3    # Edge from vertex 2 to vertex 3
3 4    # Edge from vertex 3 to vertex 4
```

### 🚀 **Usage Instructions**
1. Ensure the graph is saved in a valid format (see above examples).
2. Run the algorithm by providing the filename and source vertex.

#### For **Weighted** Graph:
```bash
python bellman_ford_weighted.py
```

#### For **Unweighted** Graph:
```bash
python bellman_ford_unweighted.py
```

---

## 🧑‍💻 Algorithm Walkthrough

1. **Input Handling**
   - Read edges from the input file.
   - For **unweighted graphs**, all edge weights are treated as **1**.

2. **Initialization**
   - Set the distance of the **source vertex** to `0`.
   - Initialize all other vertices to **infinity**.

3. **Relaxation Process**
   - Perform **V - 1** iterations, updating distances if a shorter path is found.

4. **Negative Cycle Detection**
   - After all iterations, check again for further improvements.
   - If any edge can still be relaxed, a **negative weight cycle** is present.

5. **Output**
   - Logs each iteration's updates.
   - Reports **final shortest distances**.
   - **Negative cycle detection** status.

---

## 📊 Asymptotic Time Complexity Analysis

### **Time Complexity**

Let:
- **V** = Number of vertices
- **E** = Number of edges

| Operation                  | Complexity |
|----------------------------|------------|
| Initialization             | O(V)      |
| Relaxation (V-1 iterations)| O(V * E)  |
| Negative Cycle Check       | O(E)      |

Thus, the total complexity is:  
**O(V * E)**

This applies **equally** to both the **weighted** and **unweighted** versions.

### **Space Complexity**
- **O(V)** for storing vertex distances.
- **O(E)** for storing edges.

Total: **O(V + E)**

---

## 📉 Shortcomings of the Bellman-Ford Algorithm

1. **Inefficiency on Dense Graphs**
   - For dense graphs where **E ≈ V²**, the algorithm runs in **O(V³)**.
   - **Dijkstra's algorithm** is more efficient for graphs without negative weights.

2. **Disconnected Graphs**
   - The algorithm only updates vertices **reachable** from the source.
   - Unreachable vertices will have a distance of **infinity (∞)**.

3. **Multiple Source Shortest Paths**
   - Bellman-Ford only works for a **single source** at a time.
   - For **all-pairs** shortest paths, algorithms like **Floyd-Warshall** are more appropriate.

4. **Edge Count Limitation**
   - Poor performance for graphs with extremely **large edge counts**.

---

## ✅ Example Outputs

### Weighted Graph Example
Input (weighted-digraph.txt):
```
0 1 4
0 2 5
1 2 -3
2 3 6
```

Output:
```
Starting Bellman-Ford...
Iteration 1:
Relaxing edge (0 -> 1): New distance to 1 = 4
Relaxing edge (0 -> 2): New distance to 2 = 5
Relaxing edge (1 -> 2): New distance to 2 = 1
Iteration 2:
...
Final shortest distances from source:
Node 0: Distance 0
Node 1: Distance 4
Node 2: Distance 1
Node 3: Distance 7
```

### Unweighted Graph Example
Input (unweighted-digraph.txt):
```
0 1
1 2
2 3
```

Output:
```
Starting Bellman-Ford...
Iteration 1:
Relaxing edge (0 -> 1): New distance to 1 = 1
Relaxing edge (1 -> 2): New distance to 2 = 2
Relaxing edge (2 -> 3): New distance to 3 = 3
...
Final shortest distances from source:
Node 0: Distance 0
Node 1: Distance 1
Node 2: Distance 2
Node 3: Distance 3
```

---

## 📚 Further Improvements
- **Early Stopping Optimization**: Exit if no distances are updated during a full iteration.
- **Parallel Relaxation**: Improve efficiency via multi-threading for large graphs.
- **Bidirectional Search**: Explore shortest paths from both the source and the destination.

Feel free to extend the implementation and optimize for your specific use case! 🚀

