# Modelling and Optimization Project 3

## Proposal

The project proposes the development of a chess engine capable of competitive play using the minimax algorithm with alpha-beta pruning. The core functionalities  of the project will involve board representation, move generation, position evaluation and optimal move selection.

Additionally, the project could include interactivity via a graphical interface to play against the engine. Alternatively, the chess game could be represented using the Universal Chess Interface (UCI) protocol which would allow more options for interactivity and graphical interfaces.

Implementation will be in Python (possibly using the `python-chess` library for some convenient features). This project aims to bridge the gap between theoretical concepts and practical application by applying techniques from the field of optimization, such as heuristic evaluation and search algorithms.

## Introduction

## Implementation Details

## Further Improvements

## How to Run

### Setting up the environment

1. Ensure that you have a working install of Python 3.11.8.
2. Navigate to the directory containing the project in your terminal.
3. Create a Python virtual environment by running `python3 -m venv .venv`.
4. Use the virtual environment with `source .venv/bin/activate`.
5. Install the necessary packages using `pip install -r requirements.txt`.

### Running the program (CHANGE LATER)

1. Navigate to the project directory.
2. Make sure that the virtual environment is activated. If it is not, use `source .venv/bin/activate`.
3. Run the program using `python main.py` and pass in any optional arguments.
    - You can use the `-h` flag to see the help message and the available arguments.
4. By default, the program will read the schedule requirements from the `schedule.txt` file.
    - You can instead  provide a different file by using the `--schedule` argument.
    - An example command would be `python main.py --schedule my_schedule.txt`. This would read the schedule requirements from the `my_schedule.txt` file.
4. View the schedule created by the integer programming solver in the terminal output.
