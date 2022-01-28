import random
hiddenNumber = random.randint(1, 30)
print('I am thinking of a number between 1 and 30.')

for guessesTaken in range(1, 7):
    print('Take a guess:')
    guess = int(input())

    if guess < hiddenNumber:
        print('Your guess is a bit low. try again')
    elif guess > hiddenNumber:
        print('Your guess is a bit high. try again')
    else:
        break   

if guess == hiddenNumber:
    print('Good job! You found my number in ' + str(guessesTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(hiddenNumber) + 'try again next time')

# couldnt figure out how to restart the entire thing again