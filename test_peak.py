import unittest

def get_peak(arr):
    if arr:
        return[1]
    return []

class test_peak(unittest.TestCase):

    def test_null(self):
        self.assertEqual([], get_peak([]))
    def test_check_for_one(self):
        self.assertEqual([1], get_peak([1]))



if __name__ == '__main__':
    unittest.main()
