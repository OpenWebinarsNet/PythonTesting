import unittest

from calculadora.calculator import Calculator
from calculadora.exceptions import OperationDoesntExist, MathematicalException


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()
        self.dataset_expression = (
            ((1, 1, 'add'), '1+1'),
            ((3, 1, 'subtraction'), '3-1'),
            ((4, 2, 'multiplication'), '4*2'),
            ((10, 2, 'division'), '10/2'),
        )

        self.dataset_result = (
            ((1, 1, 'add'), 2),
            ((3, 1, 'subtraction'), 2),
            ((4, 2, 'multiplication'), 8),
            ((10, 2, 'division'), 5),
        )

    def test_get_math_expression_is_working(self):

        for data in self.dataset_expression:
            expression = self.calculator.get_expression(*data[0])

            self.assertEqual(expression, data[1])

    def test_calculate_math_operation_is_working(self):
        for data in self.dataset_result:
            expression = self.calculator.calculate(*data[0])

            self.assertEqual(expression, data[1])

    def test_wrong_operation(self):
        with self.assertRaises(OperationDoesntExist):
            self.calculator.calculate(1, 1, 'sum')

    def test_bad_mathematical_result(self):
        with self.assertRaises(MathematicalException):
            self.calculator.calculate('t', 1, 'add')
            self.calculator.calculate(1, 0, 'add')

