import unittest
from wrong_number_np import find_wrong_number


class WrongNumberTest(unittest.TestCase):
    def test_wrong_middle(self):
        def_diff, wrong_nr, wrong_pos = find_wrong_number([10, 20, 30, 44, 50, 60, 70])

        self.assertEqual(def_diff, 10, "default diff")
        self.assertEqual(wrong_nr, 44, "wrong number")
        self.assertEqual(wrong_pos, 4, "wrong position")

    def test_wrong_start(self):
        def_diff, wrong_nr, wrong_pos = find_wrong_number([0, 2, 3, 4, 5, 6, 7])

        self.assertEqual(def_diff, 1, "default diff")
        self.assertEqual(wrong_nr, 0, "wrong number")
        self.assertEqual(wrong_pos, 1, "wrong position")

    def test_wrong_second(self):
        def_diff, wrong_nr, wrong_pos = find_wrong_number([1, 2.5, 3, 4, 5, 6, 7])

        self.assertEqual(def_diff, 1, "default diff")
        self.assertEqual(wrong_nr, 2.5, "wrong number")
        self.assertEqual(wrong_pos, 2, "wrong position")

    def test_wrong_before_end(self):
        def_diff, wrong_nr, wrong_pos = find_wrong_number([1, 2, 3, 4, 5, 6.5, 7])

        self.assertEqual(def_diff, 1, "default diff")
        self.assertEqual(wrong_nr, 6.5, "wrong number")
        self.assertEqual(wrong_pos, 6, "wrong position")

    def test_wrong_end(self):
        def_diff, wrong_nr, wrong_pos = find_wrong_number([1, 2, 3, 4, 5, 6, 8])

        self.assertEqual(def_diff, 1, "default diff")
        self.assertEqual(wrong_nr, 8, "wrong number")
        self.assertEqual(wrong_pos, 7, "wrong position")


if __name__ == "__main__":
    unittest.main()
