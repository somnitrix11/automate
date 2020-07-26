from random import randint

num = randint(0,20)

print('I am thinking of a number between 1 and 20')

while True:
    guess = input('Take a guess.')

    if int(guess)<num:
        print('That is too low.')

    elif int(guess)>num:
        print('That is too high.')

    else:
        break

print('This is the correct number!')
