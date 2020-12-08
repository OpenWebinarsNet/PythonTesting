import argparse

from calculadora.calculator import Calculator

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('operation', type=str, help='mathematical operation you want to do')
    parse.add_argument('num1', type=int, help='first parameter to use in your operation')
    parse.add_argument('num2', type=int, help='second parameter to use in your operation')

    arguments = parse.parse_args()

    calculator = Calculator()

    expression = calculator.get_expression(arguments.num1, arguments.num2, arguments.operation)
    result = calculator.calculate(arguments.num1, arguments.num2, arguments.operation)

    print(f'The result  is: {expression} = {str(result)}')

