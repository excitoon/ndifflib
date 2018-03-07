import unittest

import ndifflib


class test_ndifflib(unittest.TestCase):
    def test_simple(self):
        lists = [[1, 2, 3], [2, 3, 4], [1, 2, 3, 4], [2, 4], [2, 3]]
        diff = ndifflib.SequenceMatcher(None, *lists)
        self.assertEqual(diff.get_opcodes(),
            [
                ('complicated', [0, 0, 0, 0, 0], [1, 0, 1, 0, 0]),
                ('equal',       [1, 0, 1, 0, 0], [2, 1, 2, 1, 1]),
                ('complicated', [2, 1, 2, 1, 1], [3, 2, 3, 1, 2]),
                ('complicated', [3, 2, 3, 1, 2], [3, 3, 4, 2, 2])
            ])

    def test_blocks(self):
        lists = [[1, 2, 3], [2, 3, 4], [4, 5, 6], [5, 6]]
        diff = ndifflib.SequenceMatcher(None, *lists)
        self.assertEqual(diff.get_opcodes(),
            [
                ('complicated', [0, 0, 0, 0], [1, 0, 0, 0]),
                ('complicated', [1, 0, 0, 0], [3, 2, 0, 0]),
                ('complicated', [3, 2, 0, 0], [3, 3, 1, 0]),
                ('complicated', [3, 3, 1, 0], [3, 3, 3, 2])
            ])
