"""Order directed dependencies, choosing the smallest available vertex first."""

import heapq


def topological_sort(graph: dict[str, list[str]]) -> list[str]:
    """Return the lexicographically smallest valid dependency order.

    Include keys and neighbor-only vertices. Repeated edges are permitted.
    Raise ValueError on a directed cycle, including a self-loop. Preserve
    input. O(E + V*log(V + 1)) time, O(V) auxiliary space plus O(V) output.
    """
    indegree = {vertex: 0 for vertex in graph}
    for neighbors in graph.values():
        for neighbor in neighbors:
            indegree[neighbor] = indegree.get(neighbor, 0) + 1
    ready = [vertex for vertex, degree in indegree.items() if degree == 0]
    heapq.heapify(ready)
    ordered: list[str] = []
    while ready:
        vertex = heapq.heappop(ready)
        ordered.append(vertex)
        for neighbor in graph.get(vertex, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                heapq.heappush(ready, neighbor)
    if len(ordered) != len(indegree):
        raise ValueError("graph contains a directed cycle")
    return ordered


if __name__ == "__main__":
    print(topological_sort({"shop": ["cook"], "cook": ["eat"]}))
