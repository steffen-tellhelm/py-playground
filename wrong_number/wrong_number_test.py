import unittest
from wrong_number import ALGORITHMS


class WrongNumberTest(unittest.TestCase):
    def test_wrong_middle(self):
        for desc, frn in ALGORITHMS.items():
            def_diff, wrong_nr, wrong_pos, right_nr = frn([10, 20, 30, 44, 50, 60, 70])

            self.assertEqual(def_diff, 10, f"{desc} default diff")
            self.assertEqual(wrong_nr, 44, f"{desc} wrong number")
            self.assertEqual(wrong_pos, 4, f"{desc} wrong position")
            self.assertEqual(right_nr, 40, f"{desc} right number")

    def test_wrong_start(self):
        for desc, frn in ALGORITHMS.items():
            def_diff, wrong_nr, wrong_pos, right_nr = frn([0, 2, 3, 4, 5, 6, 7])

            self.assertEqual(def_diff, 1, f"{desc} default diff")
            self.assertEqual(wrong_nr, 0, f"{desc} wrong number")
            self.assertEqual(wrong_pos, 1, f"{desc} wrong position")
            self.assertEqual(right_nr, 1, f"{desc} right number")

    def test_wrong_second(self):
        for desc, frn in ALGORITHMS.items():
            def_diff, wrong_nr, wrong_pos, right_nr = frn([1, 2.5, 3, 4, 5, 6, 7])

            self.assertEqual(def_diff, 1, f"{desc} default diff")
            self.assertEqual(wrong_nr, 2.5, f"{desc} wrong number")
            self.assertEqual(wrong_pos, 2, f"{desc} wrong position")
            self.assertEqual(right_nr, 2, f"{desc} right number")

    def test_wrong_before_end(self):
        for desc, frn in ALGORITHMS.items():
            def_diff, wrong_nr, wrong_pos, right_nr = frn([1, 2, 3, 4, 5, 6.5, 7])

            self.assertEqual(def_diff, 1, f"{desc} default diff")
            self.assertEqual(wrong_nr, 6.5, f"{desc} wrong number")
            self.assertEqual(wrong_pos, 6, f"{desc} wrong position")
            self.assertEqual(right_nr, 6, f"{desc} right number")

    def test_wrong_end(self):
        for desc, frn in ALGORITHMS.items():
            def_diff, wrong_nr, wrong_pos, right_nr = frn([1, 2, 3, 4, 5, 6, 8])

            self.assertEqual(def_diff, 1, f"{desc} default diff")
            self.assertEqual(wrong_nr, 8, f"{desc} wrong number")
            self.assertEqual(wrong_pos, 7, f"{desc} wrong position")
            self.assertEqual(right_nr, 7, f"{desc} right number")


if __name__ == "__main__":
    unittest.main()
