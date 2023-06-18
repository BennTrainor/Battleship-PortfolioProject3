![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Battleships

This version of Battleships is a Python terminal game, it runs on the Code Institute mock terminal on Heroku.

Players of the game must guess coordinates to try to find the location of the computers battleships before the computer has located theirs. 



## How to Play

Upon starting the game you will see two boards, one for the player and one for the computer.
On the player board you will be able to see the location of your battleships.
You will not be able to see the battleships on the computers board.
You must input coordinates to find and sink the computer battleships.

The Battleships are placed randomly, when you begin to input your guesses the symbols on the board will change.
Once you have guessed a coordinate the '-' will change to either: an 'M' to signify a guessed coordinate that misses the computer Battleship, or an 'X' to signify that you have hit a computer Battleship.

The winner of the game is the first to sink all 4 of the opposition battleships.

## Features

## Existing Features

1. Random Battleship placement: 
        The Battleships are randomly placed on both the player and computer gameboard. 
        The player cannot see where the computer battleships are located.

2. Play against the computer
        The player is able to input coordinates of a row, then a column to identify the computers battleships.
        The computer will also make guesses against the player.

3. Input validation
        The player will not be able to input coordinates outside of the grid.
        The game will only accept numbers as a valid input. 

## Future Features

1. Not allow a coordinate to be used more than once.
2. Introduce a scoring system to keep track of how many games the player or computer have won. 
3. Allow for the user to choose different board sizes and number of battleships. 

## Data Model 

I have methods to create my gameboard, place the battleships, identify valid coordinate inputs to check for game over and to play the game ensuring that both the player and computer get equal turns. 
I have ensured the print method has been utilised to create instructions and clear spacing between game elements. 

## Testing

I have manually tested the project in the following manner:

1. Put the code through PEP8 Linter and confirmed there are no issues with the code. 
2. Tested invalid coordinates in the form of letters and numbers outside of the coordinate range.
3. Tested in the CodeAnywhere terminal and on the Heroku terminal. 

## Bugs

## Solved Bugs

1. Game was prematurely ending and showing the game over sign which I found was due to an error in the indenting. 
2. Game was not allowing to input coordinates for the location of computer battleships, I found this was due to the code to not allow a repeated coordinates guess so this code was removed. 

## Remaining Bugs

No current remaining Bugs.

## Validator Testing

Pep8
    No errors were returned from Pep8online.com

## Deployment

This app was deployed using Code Institutes mock terminal for Heroku App
1. Steps to deploy:
        - Fork or clone repository.
        - Create a new Heroku App.
        - Set the Buildbacks to Python and Nodejs in that order.
        - Link the Heroku App to the repository.
        - Click on deploy

## Credits

Code Institute for the deployment terminal. 
Code Institute for the template for Readme file. 
Websites for info on how to create a Battleships Python Game: 
        https://copyassignment.com/battleship-game-code-in-python/
        https://discuss.codecademy.com/t/excellent-battleship-game-written-in-python/430605 
        https://coderspacket.com/battleship-game-in-python 
        https://gist.github.com/w0300133/7f3e3e6f836e519f64272150ca34080c 

## Thankyou for Reading


## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
