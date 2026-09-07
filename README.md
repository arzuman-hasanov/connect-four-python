# Connect Four — Python OOP Game

A two-player **Connect Four** game implemented in Python and played directly in the terminal.

The project uses **object-oriented programming (OOP)** to separate the game board from the game logic. NumPy is used to represent and manipulate the 6×7 game grid.

## Overview

Connect Four is a two-player game where players take turns dropping pieces into one of seven columns.

The first player to connect four of their pieces horizontally, vertically, or diagonally wins the game.

This project was created as a Python programming exercise, with a focus on:

* Object-oriented programming
* Classes and methods
* NumPy arrays
* Game-state management
* Input validation
* Loops and conditionals
* Win-condition detection

## Game Board

The game uses a standard **6-row × 7-column** board.

Columns are identified using the letters `A` through `G`:

```text
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
  A   B   C   D   E   F   G
```

Players enter a column, and their piece falls to the lowest available position.

## Players

The game has two players:

* Player X
* Player O

Players alternate turns until one player wins or the board is completely filled.

## Win Conditions

A player wins by connecting four pieces in a row in any of the following directions:

### Horizontal

```text
X X X X
```

### Vertical

```text
X
X
X
X
```

### Diagonal

```text
X
  X
    X
      X
```

The program checks all four directions after every move.

## Technologies Used

* Python
* NumPy
* Object-Oriented Programming (OOP)

## Project Structure

```text
connect-four-python/
│
├── connect_four.py
├── README.md
└── requirements.txt
```

## Code Structure

The program is divided into two main classes.

### `Board`

The `Board` class is responsible for managing the game board.

Main responsibilities:

* Creating the 6×7 grid
* Displaying the board
* Reading board values
* Dropping pieces
* Checking for a winner
* Checking whether a column is full
* Resetting the board

The board is represented using a NumPy array:

```python
self.grid = np.zeros((6, 7), dtype=int)
```

The values represent:

```text
0 → Empty
1 → X
2 → O
```

### `ConnectFour`

The `ConnectFour` class controls the overall game.

It is responsible for:

* Keeping track of the active player
* Receiving player input
* Validating moves
* Updating the board
* Checking for a winner
* Detecting draws
* Starting a new game

## Win Detection

After a piece is placed, the program checks for four matching pieces in:

* Horizontal directions
* Vertical directions
* Diagonal directions

NumPy operations such as `np.all()` and `np.diagonal()` are used to simplify these checks.

For example:

```python
np.all(...)
```

checks whether all elements in a selected sequence satisfy the required condition.

## Input Validation

The game validates player input before placing a piece.

Invalid inputs include:

* A character outside `A-G`
* A column that is already full

The player is asked to enter another move when an invalid input is detected.

## Draw Detection

If every position on the board is occupied and neither player has won, the game ends in a draw.

```python
np.all(self.board.grid != 0)
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/connect-four-python.git
cd connect-four-python
```

### 2. Install the dependency

```bash
pip install numpy
```

Or install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Run the game

```bash
python connect_four.py
```

## Example

The game starts by displaying the board and asking the active player to select a column:

```text
==============================
Player X 's turn
==============================

|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
  A   B   C   D   E   F   G

enter your move(A-G):
```

## What I Learned

This project provided practice with:

* Python classes
* Object-oriented programming
* Instance variables
* Methods
* NumPy arrays
* Array indexing
* Game-state management
* Input validation
* Exception handling
* Boolean logic
* Searching for patterns in arrays

## Possible Improvements

Possible future improvements include:

* Add a computer opponent
* Implement an AI using the Minimax algorithm
* Add player score tracking
* Add a graphical user interface
* Improve the terminal interface
* Add automated tests
* Separate the game logic from the user interface
* Make the game fully platform-independent
* Add command-line options


