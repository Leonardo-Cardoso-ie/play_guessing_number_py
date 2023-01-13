import random
import math

name = input('Enter your name: ')
print('Welcome to play this game', name,'good luck!')

# globals variables to be interpreted throughout code
WINS = 0
LOSSES = 0


def try_val(input_type, input_phrase):
    try:
        input_type = int(input(input_phrase))
    except ValueError:# Instead a number the user types another character he is asked to type an integer
        print('Please use an integer for input!')
        # If it gets a value error, it is going to run this function
        input_type = try_val(input_type, input_phrase)
    return int(input_type)


"""
Create a function to run all the way from create minimum
and maximum numbers
"""
def new_game():  
    global WINS, LOSSES 
    min_number, max_number = 0, 0
    # run through the function try_val
    min_number = try_val(min_number, 'Please enter a minimum number: ')
    # Maximum number
    max_number = try_val(max_number,'Please enter maximum number: ')
    # randint() generates random integers between min and max numbers.
    rand_number = random.randint(min_number, max_number)
    # Number of chances
    # increase the user's chances according to the range between the minimum and maximum value 
    chances = math.ceil(math.sqrt(max_number - min_number))

    """
    The while loop is running while the number of chances is greater than zero
    and each turn decreases a chance of the set value
    """
    while chances >= 0:
        print(f' You have {chances} chances left!') # Say how many chances user left
        chances -= 1 # Take away one chance,when while loop is running
        guess = 0 
        # Minimum and maximum number, running stored here
        guess = try_val(guess, f'Guess a number between {min_number} and {max_number}: ')  

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
    

    
