# Connect4 Python Command Line Game

A command line implementation of the classic Connect4 game.

## Overview

This project is focused on object oriented programming, particularly class inheritance and abstract base classes.

The game has three player options: human, simple AI, and random AI - you can even have both AI's play against each other.

## Usage

### Python Usage

Once the project directory is cloned, all you have to do to play the game is run the following command on the command line:

``` python3 main.py ```

### Docker Usage

``` docker run -it connect4:v1 ```

## Game Setup

1. Picking your player type

    You will then be prompted to select the player type for player $1$.

    ```Choose the type for Player 1.```

    ```Enter Human or Random or Simple```

    The program will accept any variation of the words *human*, *simple*, or *random*. For selecting the **human** player for example, you can enter ```human``` or ```Human``` (case insensitive), or simply entering the first letter of the player: ```h``` will suffice.

2. Choosing your player name

    After selecting player type $1$, you must enter your player name.

    ``` HumanPlayer 1 enter your name ```

    * Any player name works as long as no two players have the same name, otherwise the program will throw an error. *

3. Choosing your game piece

    Select the piece you will use on the command line board.

    ``` HumanPlayer 1 enter your piece ```

    Any character will work, either a number, letter, or symbol. The only constraints are no two players can have the same piece, and you cannot use the asterik ```*``` as that is what symbolizes an empty spot on the board.

    For example, ```b```, ```0```, or ```^```.

4. Picking player type for player $2$

    You may select any of the three player types: human, simple AI or random AI. Simple AI will try to make a move on the board anywhere it can block you: the opponent. Random AI will randomly select a spot on the board to place a piece. Despite their names, the random AI is not the smartest compared to simple AI. It's harder to beat simple AI.
