class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        solution:
        Understand the pattern question is asking to check, 
        don't reverse it similar to the valid parenthesis problem
        Important: only two numbers are required for an operation 
        and the expression is always avalid means we will always get 
        those two numbers
        """
        stack_e = []
        operators = ['+', '-', '*', '/']

        def operations(op, num1, num2):
            if op == "+":
                return num1+num2
            elif op == "*":
                return num1*num2
            elif op == "-":
                return num2-num1
            else:
                return num2/num1
        
        for token in tokens:
            if token in operators:
                a = stack_e.pop()
                b = stack_e.pop()
                result = int(operations(token, a, b))
                stack_e.append(result)
            else:
                stack_e.append(int(token))
        return stack_e[0]