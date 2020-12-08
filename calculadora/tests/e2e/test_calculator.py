import unittest
from subprocess import run


class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.dataset = (
            (('add', '1', '1'), 'The result  is: 1+1 = 2'),
            (('subtraction', '1', '1'), 'The result  is: 1-1 = 0'),
            (('multiplication', '5', '2'), 'The result  is: 5*2 = 10'),
            (('division', '10', '2'), 'The result  is: 10/2 = 5.0'),
        )

    def test_calculator_program_is_working(self):
        for data in self.dataset:
            result = run(['python', '-m', 'calculadora.main', *data[0]], capture_output=True, check=True)

            self.assertEqual(data[1], result.stdout.decode('utf8').strip())

    def test_calculator_program_wrong_operation(self):
        result = run(['python', '-m', 'calculadora.main', 'sum', '1', '1'], capture_output=True)

        self.assertIn('OperationDoesntExist: The operation cannot be found', result.stderr.decode('utf8').strip())

    def test_calculator_program_wrong_arguments(self):
        result = run(['python', '-m', 'calculadora.main', 'add', 't', '1'], capture_output=True)

        self.assertIn("error: argument num1: invalid int value: 't'", result.stderr.decode('utf8').strip())

