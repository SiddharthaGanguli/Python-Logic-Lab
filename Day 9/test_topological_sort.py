import copy
from itertools import permutations, product
import unittest

from topological_sort import topological_sort


class TopologicalSortTests(unittest.TestCase):
    def test_dependency_chain_and_neighbor_only_vertex(self):
        self.assertEqual(topological_sort({"shop": ["cook"], "cook": ["eat"]}), ["shop", "cook", "eat"])

    def test_smallest_available_vertex_is_chosen(self):
        self.assertEqual(topological_sort({"b": ["d"], "a": ["c"]}), ["a", "b", "c", "d"])

    def test_empty_isolated_and_repeated_edges(self):
        self.assertEqual(topological_sort({}), [])
        self.assertEqual(topological_sort({"z": [], "a": []}), ["a", "z"])
        self.assertEqual(topological_sort({"a": ["c", "c"], "b": ["c"]}), ["a", "b", "c"])

    def test_rejects_cycles_in_any_component(self):
        for graph in ({"a": ["a"]}, {"a": ["b"], "b": ["a"]}, {"free": [], "a": ["b"], "b": ["a"]}):
            with self.subTest(graph=graph):
                with self.assertRaises(ValueError):
                    topological_sort(graph)

    def test_input_is_preserved(self):
        graph = {"b": ["c"], "a": ["c", "c"]}
        original = copy.deepcopy(graph)
        topological_sort(graph)
        self.assertEqual(graph, original)

    def test_matches_exhaustive_ordering_reference(self):
        vertices = ("a", "b", "c")
        possible_edges = [(a, b) for a in vertices for b in vertices if a != b]
        for enabled in product((False, True), repeat=len(possible_edges)):
            edges = [edge for edge, present in zip(possible_edges, enabled) if present]
            graph = {vertex: [b for a, b in edges if a == vertex] for vertex in vertices}
            valid = [list(order) for order in permutations(vertices) if all(order.index(a) < order.index(b) for a, b in edges)]
            with self.subTest(edges=edges):
                if valid:
                    self.assertEqual(topological_sort(graph), min(valid))
                else:
                    with self.assertRaises(ValueError):
                        topological_sort(graph)


if __name__ == "__main__":
    unittest.main()
