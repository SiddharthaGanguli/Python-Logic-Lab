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

## 2. Count islands in a binary grid

Write `count_islands(grid)` to count groups of land cells connected horizontally
or vertically. Land is `1`; water is `0`.

### Requirements

- The input is a rectangular list of integer lists containing only 0 and 1.
- Diagonal contact does not connect two islands.
- Raise `ValueError` for unequal row lengths or a value other than 0 or 1.
- Return `0` for empty or zero-column grids, and preserve all input cells.
- Use an explicit stack or queue to avoid relying on recursion depth.

### Examples

| Input | Expected output |
|---|---:|
| `[[1, 1, 0], [0, 1, 0], [1, 0, 1]]` | `3` |
| `[[1, 0], [0, 1]]` | `2` |
| `[[1, 1], [1, 1]]` | `1` |
| `[[], []]` | `0` |
| `[[1], []]` | `ValueError` |

### Approach and complexity

Scan the grid. Each unvisited land cell starts one new island; traverse its land
neighbors and record them as visited when adding them to the stack. For r rows
and c columns, time is O(r + r*c), including validation of empty rows. The visited
set and stack use O(r*c) auxiliary space.

[Solution](count_islands.py) · [Tests](test_count_islands.py)

## 3. Order tasks by their dependencies

Write `topological_sort(graph)` for a directed graph where an edge `a -> b` means
that `a` must appear before `b`.

### Requirements

- Include every string vertex found as a dictionary key or a neighbor.
- Return the lexicographically smallest valid order by choosing the smallest
  available vertex at every step.
- Return `[]` for an empty graph. Repeated edges are permitted.
- Raise `ValueError` for any directed cycle, including self-loops and cycles in
  disconnected components. Preserve the input.

### Examples

| Input | Expected output |
|---|---|
| `{"shop": ["cook"], "cook": ["eat"]}` | `["shop", "cook", "eat"]` |
| `{"b": ["d"], "a": ["c"]}` | `["a", "b", "c", "d"]` |
| `{"a": ["b"], "b": ["a"]}` | `ValueError` |
| `{}` | `[]` |

### Approach and complexity

Count each vertex's incoming edges and place all zero-indegree vertices in a
min-heap. Remove the smallest, emit it, and reduce its neighbors' indegrees. If
some vertices remain after the heap empties, the graph contains a cycle. Count
and remove repeated edges consistently. Time is O(E + V*log(V + 1)), with O(V)
auxiliary space and O(V) output space.

[Solution](topological_sort.py) · [Tests](test_topological_sort.py)
