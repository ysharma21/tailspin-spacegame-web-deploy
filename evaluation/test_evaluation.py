import unittest
import evaluation

class TestEvaluation(unittest.TestCase):
    def test_add(self):
        self.assertEqual(evaluation.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(evaluation.subtract(5, 3), 2)

if __name__ == '__main__':
    unittest.main()