# 🗺️ Classical & Heuristic AI Search Algorithms in Python

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Domain](https://img.shields.io/badge/Domain-Artificial%20Intelligence%20%7C%20Pathfinding-crimson.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An in-depth algorithmic library implementing foundational and heuristic **Artificial Intelligence State-Space Search Algorithms**, built by **Ammar Abdelfattah** for the **Artificial Intelligence (AI)** coursework at **Faculty of Engineering – New Ismailia National University (NINU)**.

---

## 📌 Algorithmic Formulations

The repository models problem solving as traversal across formalized state spaces $S$, action transitions $A(s)$, step cost functions $c(s, a, s')$, and goal predicates $G(s)$:

```mermaid
graph LR
    Start((Start State s0)) --> Expansion{Exploration Strategy}
    Expansion -->|FIFO Queue| BFS["Breadth-First Search (BFS)<br>Complete, Optimal for Unit Costs"]
    Expansion -->|LIFO Stack| DFS["Depth-First Search (DFS)<br>Low Memory O(bm)"]
    Expansion -->|Priority Queue by g(n)| UCS["Uniform Cost Search (Dijkstra)<br>Optimal for arbitrary costs"]
    Expansion -->|Priority Queue by h(n)| Greedy["Greedy Best-First Search<br>Guided by Heuristic h(n)"]
    Expansion -->|Priority Queue by f(n)=g(n)+h(n)| AStar["A* Search<br>Complete & Optimally Efficient"]
    
    BFS --> Goal((Goal State))
    DFS --> Goal
    UCS --> Goal
    Greedy --> Goal
    AStar --> Goal
```

### Evaluated Search Strategies:

1. **Uninformed / Blind Search Strategies**:
   - **Breadth-First Search (BFS)**: Explores shallowest nodes first using a FIFO frontier queue. Complete and optimal for uniform step costs: Time $O(b^d)$, Space $O(b^d)$.
   - **Depth-First Search (DFS)**: Deepest node exploration via LIFO stack. Space-efficient $O(bm)$ but vulnerable to infinite paths.
   - **Uniform Cost Search (UCS / Dijkstra)**: Expands the node with lowest path cost $g(n)$ using a Min-Heap priority queue. Optimal for any positive cost function.

2. **Informed / Heuristic Search Strategies**:
   - **Greedy Best-First Search**: Expands nodes closest to the goal using heuristic estimate $h(n)$.
   - **A\* Search**: Uses evaluation function:
     $$f(n) = g(n) + h(n)$$
     Guaranteed optimal and complete provided $h(n)$ is **admissible** (never overestimates true cost: $h(n) \le h^*(n)$) and **consistent** (satisfies triangle inequality: $h(n) \le c(n, a, n') + h(n')$).
   - Heuristics implemented for 2D Grid & Maze topologies:
     - Manhattan Distance: $h(n) = |x_n - x_{\text{goal}}| + |y_n - y_{\text{goal}}|$
     - Euclidean Distance: $h(n) = \sqrt{(x_n - x_{\text{goal}})^2 + (y_n - y_{\text{goal}})^2}$
     - Chebyshev / Diagonal Distance: $h(n) = \max(|\Delta x|, |\Delta y|)$

---

## 📁 Repository Structure

```text
├── search_engine/
│   ├── graph.py               # Node, Edge, and Grid representation
│   ├── uninformed.py          # BFS, DFS, Uniform Cost Search
│   └── heuristic.py           # A* Search, Greedy Best-First Search
├── demos/
│   ├── maze_pathfinder.py     # Interactive visual maze solver
│   └── benchmark.py           # Memory & expanded node counter comparison
├── requirements.txt
└── README.md
```

---

## 🚀 Quickstart

```bash
# Clone the repository
git clone https://github.com/marbdalftah72-spec/AI-Search-Algorithms-Pathfinding.git
cd AI-Search-Algorithms-Pathfinding

# Run benchmark
python demos/benchmark.py
```

---

## 👨‍💻 Author

- **Ammar Abdelfattah**
- Department of Artificial Intelligence, Faculty of Engineering
- **New Ismailia National University (NINU)**
