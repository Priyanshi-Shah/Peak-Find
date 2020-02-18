import unittest


def get_peak(arr):
    if not arr:
        return None
    if arr[0] == 1:
        return 1


class PeakTest(unittest.TestCase):

    def test_null(self):
        self.assertEqual(None, get_peak([]))

    def test_check_for_one(self):
        self.assertEqual(1, get_peak([1]))


if __name__ == '__main__':
    unittest.main()
