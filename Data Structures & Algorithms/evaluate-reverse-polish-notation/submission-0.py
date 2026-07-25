import operator
from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul, 
            "/": operator.truediv
        }

        for token in tokens:
            if token in operators:
                val1 = stack.pop()
                val2 = stack.pop()

                new_val = operators[token](val2, val1)

                stack.append(int(new_val))
            else:
                stack.append(int(token))
            
        out = stack.pop()
        return out