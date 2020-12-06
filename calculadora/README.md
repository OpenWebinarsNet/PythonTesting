## Calculator
We have built a calculator to help the children understand better the mathematics operation. 

The calculator is able to translate basic words operations to mathematical representation

```bash
python main.py add 1 1
```


This is a testing exercise, we want to ensure the correct quality of our Calculator class. 

This Calculator has two methods to obtain the mathematical expression and calculate the appropriate result.

```python
from calculator import Calculator

calculator = Calculator()
calculator.get_expression(1, 1, 'add') # return '1+1'
calculator.calculate(1, 1, 'add') # return 2
```