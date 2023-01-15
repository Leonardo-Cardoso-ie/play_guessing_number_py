# **PYTHON Number Guessing**

Python Number Guessing is a Python terminal game, wich runs in the Code Institute mock terminal on Heroku

The number guessing game is a popular game among programmers, In the number guessing game, the user selects a random number between two numbers, minimum and maximum number and the user try guesses the correct number in a maximum of chances. The game will end after x chances and if the player failed to guess the number, and then he loses the game.

The Live link can be found here: https://python-number-guessing.herokuapp.com/

![responsive](https://user-images.githubusercontent.com/96269648/212520645-d90a17c4-7fb8-4992-a5ae-c9e33ff40538.png)


## **How to play**

In this version of Python number Guessing, the player enters their name and when entering the name, the user receives a welcome message and good luck, then the computer asks the user to enter a minimum number, after entering the number, the user is asked again to insert a maximum number, after that the user presses "enter", and receives the feedback message that he has a certain number of chances (this number of chances varies, as it depends on the range between the smallest and the largest number , that is, the greater the range, the greater the player's chances). During the game, the user decreases his number of chances to guess the number, each time his chances reach zero, the game ends



## **Features** 
### **Existing Features**

User interface display 

  - The user is asked to enter his name
  - When entering the name, the player receives a welcome message and good luck
  - After the welcome message, the player is asked to enter a minimum number and then enter a maximum number.

  
  ![screen1](https://user-images.githubusercontent.com/96269648/212523974-a37df5d3-4372-4ab9-a354-09ca9c69a43b.png) 
 
 

  - After the player enters the two minimum and maximum numbers, the message appears: You have x chances left! 

  - Guess a number between x and y.
  - The player enters the number and while he does not guess the number, the app gives feedback:
  - Your Guess is lower than my number or your Guess is upper than my number!


![screen3](https://user-images.githubusercontent.com/96269648/212525297-3998814a-5770-452f-bb92-3fe8946aadd7.png)



  - According to the user's attempts to guess the number, the number of chances decreases until it reaches zero. 

  - The game ends when the user guesses the number or when he loses to the computer and his chances reach zero.
  - When the game is over, the user checks result on the scoreboard .
  - the user receives feedback, Yes - to continue or no - to quit game
  - If yes, the game continues, if not, the game stops and the user receives a message: See you next time!
  
  

![Imagem1](https://user-images.githubusercontent.com/96269648/212526873-cccd16d1-321f-460e-aa7b-25dc74bfa6fd.png)


### Input validation and error - checking:
  - If the player enters a value that is not a number, the display automatically shows a message 

  - Please use an integer for input!
  -As long as the player does not enter an integer, the message is repeated and the game continues after typing an integer.


 ![screen4](https://user-images.githubusercontent.com/96269648/212527677-a2f4feeb-1482-43a6-a654-3cbece93086c.png)
 
 

 ##Testing
- HTML
  - No errors were returned when passing through the official] https://validator.w3.org/
  - CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?
  - Lighthouse test
  
  ![Imag000](https://user-images.githubusercontent.com/96269648/187071421-14520190-3e09-4700-a7a6-4aac6381319a.png)

  
## Deployment


- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 



## Credits 

The logo image was taken from icons8.com


# Special Thanks

- My special thanks go out to my family, my wife and my son, they know how hard it has been but they believe in me and the Code Institute 