from random import randrange
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])

while True:
    try:
        num = int(input(f'Enter any number between {start}-{end} : '))
        random_num = randrange(start, end)

        print(f'User Input : {num}')
        print(f'Random Number Generated : {random_num}')

        if num == random_num:
            print("Success")
            break

        else:
            print("Failure")
            continue

    except ValueError:
        print(f'Enter integer between {start}-{end}')
