"""Check whether an undirected graph can be colored with two colors."""

from collections import deque


def is_bipartite(graph: dict[str, list[str]]) -> bool:
    """Return whether each edge can connect vertices of different colors.

    Treat every listed edge as undirected, even if only one direction appears.
    Include neighbor-only vertices; disconnected and empty graphs are valid.
    Self-loops make the result False. Preserve input. O(V + E) expected time
    and auxiliary space, including the normalized undirected adjacency sets.
    """
    neighbors: dict[str, set[str]] = {vertex: set() for vertex in graph}
    for vertex, adjacent in graph.items():
        for neighbor in adjacent:
            neighbors[vertex].add(neighbor)
            neighbors.setdefault(neighbor, set()).add(vertex)

    colors: dict[str, int] = {}
    for start in neighbors:
        if start in colors:
            continue
        colors[start] = 0
        pending = deque([start])
        while pending:
            vertex = pending.popleft()
            for neighbor in neighbors[vertex]:
                if neighbor not in colors:
                    colors[neighbor] = 1 - colors[vertex]
                    pending.append(neighbor)
                elif colors[neighbor] == colors[vertex]:
                    return False
    return True


if __name__ == "__main__":
    print(is_bipartite({"a": ["b", "d"], "b": ["c"], "c": ["d"]}))
