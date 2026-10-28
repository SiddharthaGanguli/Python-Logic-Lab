"""Find a shortest route through a directed, unweighted graph."""

from collections import deque


def shortest_path(graph: dict[str, list[str]], start: str, goal: str) -> list[str] | None:
    """Return a minimum-edge path, or None if goal is unreachable.

    Missing keys have no outgoing edges. A vertex is reachable from itself,
    even when absent from the graph. Ties follow each adjacency list's order.
    The graph is not modified. Worst-case O(V + E) time and O(V) auxiliary
    space over reachable vertices and edges, plus O(V) path output.
    """
    parents: dict[str, str | None] = {start: None}
    pending = deque([start])
    while pending:
        vertex = pending.popleft()
        if vertex == goal:
            path: list[str] = []
            current: str | None = goal
            while current is not None:
                path.append(current)
                current = parents[current]
            path.reverse()
            return path
        for neighbor in graph.get(vertex, []):
            if neighbor not in parents:
                parents[neighbor] = vertex
                pending.append(neighbor)
    return None


if __name__ == "__main__":
    print(shortest_path({"A": ["B", "C"], "B": ["D"], "C": ["D"]}, "A", "D"))
