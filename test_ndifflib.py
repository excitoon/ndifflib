import unittest

import ndifflib


class test_ndifflib(unittest.TestCase):
    def testSimple(self):
        lists = [[1, 2, 3], [2, 3, 4], [1, 2, 3, 4], [2, 4], [2, 3]]
        diff = ndifflib.SequenceMatcher(None, *lists)
        self.assertEqual(diff.get_opcodes(),
            [
                ('complicated', [0, 0, 0, 0, 0], [1, 0, 1, 0, 0]),
                ('equal',       [1, 0, 1, 0, 0], [2, 1, 2, 1, 1]),
                ('complicated', [2, 1, 2, 1, 1], [3, 2, 3, 1, 2]),
                ('complicated', [3, 2, 3, 1, 2], [3, 3, 4, 2, 2])
            ])
