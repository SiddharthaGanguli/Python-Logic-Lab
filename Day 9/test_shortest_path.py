import copy
from itertools import product
import unittest

from shortest_path import shortest_path


class ShortestPathTests(unittest.TestCase):
    def test_ties_follow_adjacency_order(self):
        graph = {"A": ["C", "B"], "B": ["D"], "C": ["D"]}
        self.assertEqual(shortest_path(graph, "A", "D"), ["A", "C", "D"])

    def test_direct_route_beats_longer_route(self):
        graph = {"A": ["B", "D"], "B": ["C"], "C": ["D"]}
        self.assertEqual(shortest_path(graph, "A", "D"), ["A", "D"])

    def test_cycles_duplicates_and_missing_neighbor_keys(self):
        graph = {"A": ["A", "B", "B"], "B": ["A", "C"]}
        self.assertEqual(shortest_path(graph, "A", "C"), ["A", "B", "C"])

    def test_absent_vertices_and_empty_graph(self):
        self.assertEqual(shortest_path({}, "A", "A"), ["A"])
        self.assertIsNone(shortest_path({}, "A", "B"))
        self.assertIsNone(shortest_path({"A": ["B"]}, "B", "A"))

    def test_input_is_preserved(self):
        graph = {"A": ["B", "B"], "B": []}
        original = copy.deepcopy(graph)
        shortest_path(graph, "A", "B")
        self.assertEqual(graph, original)

    def test_matches_repeated_distance_relaxation(self):
        vertices = ("A", "B", "C")
        possible_edges = [(a, b) for a in vertices for b in vertices if a != b]
        for enabled in product((False, True), repeat=len(possible_edges)):
            edges = [edge for edge, present in zip(possible_edges, enabled) if present]
            graph = {vertex: [b for a, b in edges if a == vertex] for vertex in vertices}
            for start in vertices:
                distances = {vertex: float("inf") for vertex in vertices}
                distances[start] = 0
                for _ in range(len(vertices) - 1):
                    previous = distances.copy()
                    for first, second in edges:
                        distances[second] = min(distances[second], previous[first] + 1)
                for goal in vertices:
                    with self.subTest(edges=edges, start=start, goal=goal):
                        path = shortest_path(graph, start, goal)
                        if distances[goal] == float("inf"):
                            self.assertIsNone(path)
                        else:
                            self.assertEqual((path[0], path[-1]), (start, goal))
                            self.assertEqual(len(path) - 1, distances[goal])
                            self.assertTrue(all(b in graph[a] for a, b in zip(path, path[1:])))


if __name__ == "__main__":
    unittest.main()
