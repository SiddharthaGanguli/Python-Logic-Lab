# Day 9 — Graphs and grid traversal

Practice reachability, connected regions, dependency ordering, and two-coloring.
Graphs use string vertex labels and adjacency lists. Complexity uses the usual
constant-cost hashing and label-comparison model; long labels can add work.

## 1. Find a shortest route in an unweighted graph

Write `shortest_path(graph, start, goal)` to return a path with the fewest edges
between two vertices in a directed graph.

### Requirements

- The graph is a dictionary of string labels to lists of outgoing neighbor labels.
- Missing dictionary keys have no outgoing edges. Do not modify the graph.
- Return a list including both endpoints, or `None` if no route exists.
- Return `[start]` when `start == goal`, even if the label is not in the dictionary.
- Resolve equal-length routes by breadth-first discovery in adjacency-list order.
- Handle cycles, self-loops, repeated edges, and disconnected components.

### Examples

| Graph | Start, goal | Expected output |
|---|---|---|
| `{"A": ["B", "C"], "B": ["D"], "C": ["D"]}` | `"A", "D"` | `["A", "B", "D"]` |
| `{"A": ["B"]}` | `"B", "A"` | `None` |
| `{}` | `"A", "A"` | `["A"]` |

### Approach and complexity

Use a FIFO queue to visit vertices in increasing distance from the start. Record
each vertex's parent when it is first discovered, then follow the parents backward
from the goal. For V reachable vertices and E outgoing edges, the worst-case work
is O(V + E), with O(V) auxiliary space and up to O(V) path output.

[Solution](shortest_path.py) · [Tests](test_shortest_path.py)
