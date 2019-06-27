# Yilin Wang
# pre_lecture assignment
# BMES T580

import random
import math

print('**********************************')
print('  GUESS_THAT_PRIMER GAME  ')
print('**********************************')
print()


DNA = ['A','G','C','T'] # DNA base
# set the initial sequence as a empty string
# the base will be added into this empty string as a target DNA sequence.
the_primer = ''

# use the for loop to generate the random DNA sequence ( the string need to be 5 letters long)
for i in range (0,5):
    the_primer +=random.choice(DNA)

#set up the initial values
guess = 'NNNNN'


# asking the users' name to begin the guess game
name = input('What is your name? ')
# calculate the length of the primer (should be 5 in this game).
target_length= len(the_primer)

# print the hint
print('The number of letters for the Target DNA sequence is {}.'.format(target_length))
print ('The DNA base is {}.'. format(DNA))
# set up a while loop to define while the DNA sequence that user guessing is different than the random DNA (the_primer),
#---it is allow the user to take another guess.
while guess != the_primer:
    guess_text = input('Guess a primer DNA sequence: ') # asking the user to generate a DNA sequence (5 letters long)
    guess = guess_text
    # get the length of the guess DNA sequence
    guess_length = len(guess)
# using if loop to split the situations (correctly or incorrectly)
# if the user's answer is incorrect, the system will allow another guess
# if the user has teh correct answer, the user win and exit the game

    if guess != the_primer:
        # set up the initial value of the counter number (the number of correct letters)
        count = 0
        # get the minimum length of the string
        comparing_range = min(target_length,guess_length)
        # using for loop to check if there are any  correct letter, and count the number of correct letters.
        for q in range (comparing_range):
            if the_primer[q] == guess[q]:
                count = count+1
        # print('Your guess of ' + guess + ' was incorrect.' + the number of correct letters is + count)
        print('Sorry {}. Your guess {} is incorrect. The number of correct letters is {}. Play again? '.format(name, guess,count))
    else:
        print('Excellent work {}! you win! The target DNA sequence is {}!'.format(name, guess))

print('Done!!!')
