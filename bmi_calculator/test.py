import unittest
from functions import calculate_bmi, interpret_bmi

class TestBMICalculator(unittest.TestCase):

    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)

    def test_interpret_bmi(self):
        self.assertEqual(interpret_bmi(22.86), "Normāls svars")

if __name__ == "__main__":
    unittest.main()
