import copy
from itertools import combinations, product
import unittest

from bipartite_graph import is_bipartite


class BipartiteGraphTests(unittest.TestCase):
    def test_even_and_odd_cycles(self):
        self.assertTrue(is_bipartite({"a": ["b", "d"], "b": ["c"], "c": ["d"]}))
        self.assertFalse(is_bipartite({"a": ["b", "c"], "b": ["c"]}))

    def test_empty_isolated_and_neighbor_only_vertices(self):
        self.assertTrue(is_bipartite({}))
        self.assertTrue(is_bipartite({"alone": []}))
        self.assertTrue(is_bipartite({"a": ["b"]}))

    def test_asymmetric_edges_and_duplicates(self):
        self.assertTrue(is_bipartite({"a": ["b", "b"], "c": ["b"]}))

    def test_self_loop_and_disconnected_odd_component(self):
        self.assertFalse(is_bipartite({"a": ["a"]}))
        self.assertFalse(is_bipartite({"free": ["leaf"], "a": ["b", "c"], "b": ["c"]}))

    def test_input_is_preserved(self):
        graph = {"a": ["b", "b"], "c": ["b"]}
        original = copy.deepcopy(graph)
        is_bipartite(graph)
        self.assertEqual(graph, original)

    def test_matches_exhaustive_two_color_assignments(self):
        vertices = ("a", "b", "c", "d")
        possible_edges = list(combinations(vertices, 2))
        for enabled in product((False, True), repeat=len(possible_edges)):
            edges = [edge for edge, present in zip(possible_edges, enabled) if present]
            graph = {vertex: [b for a, b in edges if a == vertex] for vertex in vertices}
            expected = any(
                all(colors[vertices.index(a)] != colors[vertices.index(b)] for a, b in edges)
                for colors in product((0, 1), repeat=len(vertices))
            )
            with self.subTest(edges=edges):
                self.assertEqual(is_bipartite(graph), expected)


if __name__ == "__main__":
    unittest.main()
