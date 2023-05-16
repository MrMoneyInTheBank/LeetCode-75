"""
You are given an array of strings tokens that represents an 
arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents 
the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

def evalRPN(tokens):
    operations = {
        "*": lambda x, y: x*y,
        "+": lambda x, y: x+y,
        "-": lambda x, y: x-y,
        "/": lambda x, y: float(x)/y
    }
    stack = []
    for token in tokens:
        if token not in operations:
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            result = operations[token](left, right)
            stack.append(int(result))
    return stack.pop()

# Time | Space: O(n) | O(n)
# Keep track of the integers as they are added to the stack. Once you reach an operator
# extract the lambda function mapped to that operation in the dicitonary and append that 
# to the stack