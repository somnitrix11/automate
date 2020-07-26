from itertools import count

try:
    print('Enter an integer:')
    integer = int(input())


    def collatz(number):
        if number % 2 == 0:
            return int(number/2)
        elif number % 2 == 1:
            return 3*int(number)+1

    sum=collatz(integer)

    for i in count():

        if sum != 1:
            sum= collatz(sum)
            print(sum)
        else:
            break

    print('The function returns 1.')

except ValueError:
    print('Please enter an integer.')
