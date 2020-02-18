import unittest


def get_peak(arr):
    if not arr:
        return None
    if len(arr)>1:
        return max(arr)
    else:
        return arr[0]


class PeakTest(unittest.TestCase):

    def test_null(self):
        self.assertEqual(None, get_peak([]))

    def test_check_for_one(self):
        self.assertEqual(1, get_peak([1]))

    def test_check_for_two(self):
        self.assertEqual(2, get_peak([2]))

    def test_check_for_two_elements(self):
        self.assertEqual(2, get_peak([1,2]))




if __name__ == '__main__':
    unittest.main()
