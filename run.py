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
    chances -= 1
    guess = int(input('Guess a number between _ and _ '))    

# Tell us if we guessed too high or low

# Tell us if we are right or wrong

# Prompt if win or lose

# Keep score and give option to retry
