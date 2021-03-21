
def calc(user_input):
    nums = ''.join(x for x in user_input.split())
    try:
        print(eval(nums))
    except Exception:
        print('Invalid expression')


def main():
    while True:
        user_input = input()
        if user_input == '/exit':
            print('Bye!')
            exit()
        elif user_input == '/help':
            print('Smart calculator, but not yet')
            continue
        elif user_input.startswith('/'):
            print('Unknown command')
            continue
        if user_input:
            calc(user_input)


if __name__ == '__main__':
    main()
