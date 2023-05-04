# Memory Game With NumPy

> A simple memory game where the player needs to match pairs of numbers that are randomly generated using NumPy.

## How to install and run the game?

1. Clone the source code to your local machine:

   `git clone `[https://github.com/shrfa/Memory-Game-NumPy.git](https://github.com/shrfa/Memory-Game-NumPy.git)

2. install NumPy on your system if it's not installed yet. Use the command below:

   `pip install numpy`

3. run the application by `python3 game.py`

### Gameplay:

1. The game board is a square grid of 4x4 cells.
2. The game randomly generates 8 pairs of numbers between 1 and 8, and places them in random cells on the board.
3. The player would see the numbers but after 5 sec all the cells become blank so the player should memories the pairs positions and give the number of rows and cols of them.
4. If the numbers in the cells match, they become -1 and the player earns a point. If not they loos.
5. The game ends when all pairs have been found and the player's score is displayed at the end of the game.
