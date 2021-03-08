import unittest
from Calculator import Calculator
from CsvReader import CSVReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add(self):
        self.assertEqual(self.calculator.add(3, 3), 6)
        self.assertEqual(self.calculator.result, 6)

    def test_subtraction(self):
        testData = CSVReader('/CSV_files/subtraction.csv').data
        for row in test_data:
        self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), row['Result'] )
        self.assertEqual(self.calculator.result, row['Result'])

    def test_division(self):
        self.assertEqual(self.calculator.subtract(3, 3), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_square(self):
        self.assertEqual(self.calculator.subtract(3, 3), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_Square_root(self):
        self.assertEqual(self.calculator.subtract(3, 3), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main':
    unittest.main()
