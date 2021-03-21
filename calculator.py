
def calc(user_input):
    nums = ''.join(x for x in user_input.split())
    print(eval(nums))


def main():
    while True:
        user_input = input()
        if user_input == '/exit':
            print('Bye!')
            exit()
        if user_input == '/help':
            print('Smart calculator, but not yet')
            continue
        if user_input:
            calc(user_input)


if __name__ == '__main__':
    main()
