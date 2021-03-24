from collections import deque
from string import ascii_letters, digits


class Calc:
    operands = ascii_letters + digits
    variables = {}

    def calc(self, raw_input):
        user_input = self.prepare_expression(raw_input)
        if not user_input:
            return False
        rpn = self.convert_to_rpn(user_input)
        stack = deque()
        for i in rpn:
            if i[0] in digits or (i[0] == '-' and len(i) > 1):
                stack.append(i)
            elif i in self.variables:
                stack.append(self.variables.get(i))
            else:
                second, first, result = int(stack.pop()), int(stack.pop()), None
                if i == '+':
                    result = first + second
                elif i == '-':
                    result = first - second
                elif i == '*':
                    result = first * second
                elif i == '/':
                    result = first // second
                stack.append(result)
        print(stack[-1])

    # Reverse Polish notation (RPN)
    @staticmethod
    def convert_to_rpn(user_input):
        operators = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}
        stack, result = deque(), deque()

        for i in user_input:
            if i[0] in Calc.operands:
                result.append(i)
            elif not stack or stack[-1] == '(':
                stack.append(i)
            elif operators[i] > operators[stack[-1]]:
                stack.append(i)
            elif i in list(operators.keys())[:4] and operators[i] <= operators[stack[-1]]:
                while stack and stack[-1] != '(' and operators[i] <= operators[stack[-1]]:
                    result.append(stack.pop())
                stack.append(i)
            elif i == '(':
                stack.append(i)
            elif i == ')':
                while stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
        for i in range(len(stack)):
            if stack[-1] in ')(':
                print('Syntax error')
                exit()
            result.append(stack.pop())
        return result

    def declare_variable(self, raw_input):
        var, _, val = raw_input.partition('=')
        var, val = var.strip(), val.strip()
        if not var.isalpha():
            print('Invalid identifier')
            return
        if not (val.isalpha() or val.isnumeric()) or \
                val.isalpha() and not self.variables.get(val):
            print('Invalid assignment')
            return
        self.variables[var] = val if val.isnumeric() else self.variables.get(val)

    def prepare_expression(self, raw_input):
        if raw_input.find('//') != -1 or raw_input.find('**') != -1:
            print('Invalid expression')
            return False

        user_input = ''.join(x if x in Calc.operands else f' {x} ' for x in raw_input).split()

        if not user_input[0].isalpha() and not user_input[0].isnumeric():
            print('Invalid identifier')
            return False

        return user_input


def main():
    calc = Calc()
    while True:
        raw_input = input()
        if raw_input == '/exit':
            print('Bye!')
            exit()
        elif raw_input == '/help':
            print('Calculator with variables support')
            continue
        elif raw_input.startswith('/'):
            print('Unknown command')
            continue
        elif raw_input.find('=') != -1:
            calc.declare_variable(raw_input)
        elif raw_input:
            calc.calc(raw_input)


if __name__ == '__main__':
    main()
