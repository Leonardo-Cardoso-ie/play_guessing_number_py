import random

name = input('Enter your name: ')
print('Welcome to play this game', name,'good luck!')

# globals variables to be interpreted throughout code
WINS = 0
LOSSES = 0




"""
Create a function to run all the way from create minimum
and maximum numbers
"""
def new_game():  
    global WINS, LOSSES 
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
            WINS += 1 # To add one to the WINS
            print(f'WINS - {WINS}  Losses - {LOSSES}') # Scoreboard
           
            """
            Prompt the user to play again and show how
            many times won and loose.
            """
            play_again = input('Would you like to play again?')
            """
            The code was modified to make it easier for the user,
            that instead of typing the word yes to continue the game,
            he just clicks on the letter y or number 1
            """
            if 'y'.lower() in play_again or '1' in play_again:
                new_game() # If statement say yes, run this function again
            else:
                quit() # When user say no, jus quit the game
    LOSSES += 1
    print('Sorry you ran out of chances!') # Notifies the user that his chances are over
    WINS += 1 # To add one to the WINS
    print(f'WINS - {WINS}  Losses - {LOSSES}')
    play_again = input('Would you like to play again?') # Give the user option to play again 
    """
    The code was modified to make it easier for the user,
    that instead of typing the word yes to continue the game,
     he just clicks on the letter y or number 1
    """
    if 'y'.lower() in play_again or '1' in play_again:
        new_game()
    else:
        quit()


new_game()            
    

    # Keep score and give option to retry
