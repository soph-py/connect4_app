# Connect4 Python Command Line Game

A command line implementation of the classic Connect4 game written in pure Python.

## Overview

This project is focused on object oriented programming, particularly class inheritance and abstract base classes. It is built in pure Python, using only built-in modules from the Python Standard Library.

The game has three player options: human, basic AI, and random AI - you can even have both AI's play against each other.

## Usage - Unix/Linux Operating Systems

Clone the repository

```bash:
https://github.com/sophiatierney/connect4_app.git
```

Once the project repo is cloned, cd into the root directory:

```bash:
cd connect4_app/Connect4/ 
```

### Python Usage

To play the game, run the following command in the terminal:

```bash:
python3 main.py 
```

### Docker Usage

Alternatively, you can run the docker image by running the command below in the terminal:

```bash:
docker run -it connect4:v1 
```

## Game Setup

1. Picking your player type

    You will then be prompted to select the player type for player $`1`$.

    ```Choose the type for Player 1.```

    ```Enter Human or Random or Basic```

    The program will accept any variation of the words *human*, *basic*, or *random*. For selecting the **human** player for example, you can enter ```human``` or ```Human``` (case insensitive), or simply entering the first letter of the player: ```h``` will suffice.

2. Choosing your player name

    After selecting player type $`1`$, you must enter your player name.

    ``` HumanPlayer 1 enter your name ```

    - *Any player name works as long as no two players have the same name, otherwise the program will throw an error.*

3. Choosing your game piece

    Select the piece you will use on the command line board.

    ``` HumanPlayer 1 enter your piece ```

    Any character will work, either a number, letter, or symbol. The only constraints are no two players can have the same piece, and you cannot use the asterik ```*``` as that is what symbolizes an empty spot on the board.

    For example, ```b```, ```0```, or ```^```.

4. Picking player type for player $`2`$

    You may select any of the three player types: human, basic AI or random AI. basic AI will try to make a move on the board anywhere it can block you: the opponent. Random AI will randomly select a spot on the board to place a piece. Despite their names, the random AI is not the smartest compared to basic AI. It's harder to beat basic AI.

## Project File Structure

```bash:
.
├── Connect4
│   ├── Connect4Game
│   │   ├── __init__.py
│   │   ├── src
│   │   │   ├── __init__.py
│   │   │   ├── board.py
│   │   │   ├── game.py
│   │   │   ├── move.py
│   │   │   └── players
│   │   │       ├── __init__.py
│   │   │       ├── basic_ai.py
│   │   │       ├── human_player.py
│   │   │       ├── player.py
│   │   │       └── random_ai.py
│   │   └── test
│   │       ├── __init__.py
│   │       ├── test_basic_ai.py
│   │       ├── test_board.py
│   │       ├── test_human_player.py
│   │       └── test_random_ai.py
│   ├── Dockerfile
│   ├── config_files
│   │   └── connect4.txt
│   ├── env
│   ├── main.py
│   ├── pyproject.toml
│   ├── setup.cfg
│   └── setup.py
├── LICENSE.md
└── README.md
7 directories, 23 files
```
