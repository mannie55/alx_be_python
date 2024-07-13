import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def tearDown(self):
        pass

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(-10, -5), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(10, -5), -50)
        self.assertEqual(self.calc.multiply(-10, -5), 50)
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(-10, 5), -2)
        self.assertEqual(self.calc.divide(-10, -5), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(10, 0), None)
        # or
        # with self.assertRaised(ValueError):
        #     calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()