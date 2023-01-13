import random

name = input('Enter your name: ')
print('Welcome to play this game', name,'good luck!')

# Minimum number
min_number = int(input('Please enter minimum number: '))
# Maximum number
max_number = int(input('Please enter maximum number: '))
# randint() generates random integers between min and max numbers.
rand_number = random.randint(min_number, max_number)
# Number of chances
chances = 3

"""
The while loop is running while the number of chances is greater than zero
and each turn decreases a chance of the set value
"""
while chances >= 0:
    chances -= 1 # Take away one chance,when while loop is running
    # Minimum and maximum number, running stored here
    guess = int(input(f'Guess a number between {min_number} and {max_number}:'))    

# Tell us if we guessed too high or low
    if guess > rand_number:
        print('Too high!')
    elif guess < rand_number:
        print('Too low!')     
# Tell us if user are right or wrong
    elif guess == rand_number:
        print('You guesses correct!')
        """
        Prompt the user to play again and show how
        many times won and loose.
        """
        play_again = input('Would you like to play again?')
# Prompt if win or lose

# Keep score and give option to retry
