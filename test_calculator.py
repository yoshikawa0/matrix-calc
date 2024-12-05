import unittest
from calculator import MatrixCalculator

class TestMatrixCalculator(unittest.TestCase):
    def test_add_matrices(self):
        calc = MatrixCalculator()
        result = calc.add_matrices([[1, 2]], [[3, 4]])
        self.assertEqual(result, [[4, 6]])

if __name__ == "__main__":
    unittest.main()
