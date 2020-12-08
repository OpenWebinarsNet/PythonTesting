from calculadora.exceptions import OperationDoesntExist, MathematicalException


class Calculator:
    _OPERATIONS = {
        'add': '+',
        'subtraction': '-',
        'multiplication': '*',
        'division': '/'
    }

    def get_expression(self, num1: int, num2: int, operation: str) -> str:
        try:
            opr: str = self._OPERATIONS[operation]
        except KeyError:
            raise OperationDoesntExist('The operation cannot be found')

        expression = f'{num1}{opr}{num2}'
        return expression

    def calculate(self, num1: int, num2: int, operation: str) -> int:
        expression = self.get_expression(num1, num2, operation)

        try:
            result = eval(expression)
            return result
        except Exception as e:
            raise MathematicalException(f'The mathematical operation is not correct: {e}')