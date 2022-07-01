import unittest
from main import sort


class TestSort(unittest.TestCase):

    def test_sort(self):
        self.assertEqual(sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(sort([0, -5, 3]), [-5, 0, 3])
        self.assertEqual(sort([]), [])
        self.assertEqual(sort([3.5, 3.4, 2.1]), [2.1, 3.4, 3.5])
        self.assertEqual(sort(["a", "g", "b", 'c']), ['a', 'b', 'c', 'g'])


if __name__ == '__main__':
    unittest.main()
