import random

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('   GUESS THAT NUMBER GAME')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('Ready?')
print('GO')

# get the random number as the target number
target = random.randint(0, 100)
# get the initial guess number
guess = -1

# asking the user's name
user_name = input('What is your name? ')
print ('Nice to meet you {}'. format(user_name))


# using the while loop to identify if the guess number is equal to the target number

while guess != target:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = guess_text
    # using a if function to split the difference situations (smaller, greater,or equal)
    if guess < target:
    # if the guess number is smaller than the target, print('Your guess of ' + guess + ' is too LOW.')
        print('Woops, sorry {}, your guess of {} is too LOW.'.format(user_name, guess))

    elif guess > target:
    # if the guess number is bigger than the target, print('Your guess of ' + guess + ' is too HIGH.')
        print('Woops, sorry {}, your guess of {} is too HIGH.'.format(user_name, guess))

    else:
    # if the guess number is equal to the target, print('Excellent work' + 'you win'+ 'it is '+ guess. )
        print('Excellent work {}! You win! It is {}!'.format(user_name, guess))

print('Done!!!')