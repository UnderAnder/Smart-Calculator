
def main():
    while True:
        user_input = input()
        if user_input == '/exit':
            print('Bye!')
            exit()
        if user_input:
            print(sum(int(x) for x in user_input.split()))


if __name__ == '__main__':
    main()
