class Calc:
    variables = {}

    @staticmethod
    def calc(user_input):
        identifier = user_input.split()[0]
        if user_input.find('//') != -1:
            print('Invalid expression')
        if not identifier.isalpha() and not identifier.isnumeric():
            print('Invalid identifier')
            return
        try:
            nums = ''.join(Calc.variables.get(x) if x.isalpha() else x for x in user_input.split())
            print(int(eval(nums)))
        except TypeError:
            print('Unknown variable')
        except Exception:
            print('Invalid expression')

    @staticmethod
    def declare_variable(user_input):
        var, eq, val = user_input.partition('=')
        var, val = var.strip(), val.strip()
        if not var.isalpha():
            print('Invalid identifier')
            return
        if not (val.isalpha() or val.isnumeric()) or \
                val.isalpha() and not Calc.variables.get(val):
            print('Invalid assignment')
            return
        Calc.variables[var] = val if val.isnumeric() else Calc.variables.get(val)


def main():
    calc = Calc()
    while True:
        user_input = input()
        if user_input == '/exit':
            print('Bye!')
            exit()
        elif user_input == '/help':
            print('Calculator with variables support')
            continue
        elif user_input.startswith('/'):
            print('Unknown command')
            continue
        elif user_input.find('=') != -1:
            calc.declare_variable(user_input)
        elif user_input:
            calc.calc(user_input)


if __name__ == '__main__':
    main()
