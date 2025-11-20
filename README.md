# Python Projects Collection

A collection of interactive Python console applications demonstrating fundamental programming concepts including loops, conditionals, functions, input validation, and algorithm design.

## Projects

### 1. Number Guessing Game 🎮

An interactive console-based game where players guess a randomly generated number within a specified range.

**Features:**
- Multiple difficulty levels (Easy, Medium, Hard, Expert)
- Configurable attempt limits based on difficulty
- User-friendly feedback with hints
- Input validation to prevent errors
- Replay functionality

**How to Run:**
```bash
python number_guessing_game.py
```

**Gameplay:**
- Select a difficulty level (1-4)
- Guess the secret number within the allowed attempts
- Receive feedback on whether your guess is too high or too low
- Get hints when you're close to the answer

**Difficulty Levels:**
- **Easy**: Numbers 1-50, 10 attempts
- **Medium**: Numbers 1-100, 7 attempts
- **Hard**: Numbers 1-200, 5 attempts
- **Expert**: Numbers 1-500, 3 attempts

### 2. Grade Calculator 📊

A command-line tool that computes weighted averages for course grades using user-provided inputs.

**Features:**
- Weighted average calculation for multiple assignments
- Input validation to prevent calculation errors
- Letter grade conversion (A+ to F)
- GPA conversion (4.0 scale)
- Modular design for easy expansion
- Support for any number of assignments

**How to Run:**
```bash
python grade_calculator.py
```

**Usage:**
1. Enter assignment names, scores (0-100), and weights (0-100)
2. Type 'done' when finished entering assignments
3. View your weighted average, letter grade, and GPA
4. Calculate grades for multiple courses

**Example:**
```
Assignment: Midterm Exam
Score: 85
Weight: 30

Assignment: Final Project
Score: 92
Weight: 40

Assignment: Homework
Score: 88
Weight: 30
```

## Technologies Used

- **Python 3.x**
- Standard library modules:
  - `random` - For number generation in the guessing game
  - Built-in functions for input/output handling

## Key Programming Concepts Demonstrated

### Number Guessing Game
- Loops (while loops for game flow)
- Variables and data types
- Conditionals (if/elif/else statements)
- Random number generation
- Input/output handling
- Function design and modularity

### Grade Calculator
- Functions for code organization
- Loops for data collection
- Conditionals for validation and logic
- Input validation and error handling
- Algorithm design (weighted average calculation)
- Modular code structure for future expansion

## Project Structure

```
project/
├── number_guessing_game.py    # Number guessing game implementation
├── grade_calculator.py         # Grade calculator implementation
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies (none required)
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Installation

1. Clone or download this repository
2. Ensure Python 3.6+ is installed on your system
3. Run the desired script using Python

```bash
# Check Python version
python --version

# Run Number Guessing Game
python number_guessing_game.py

# Run Grade Calculator
python grade_calculator.py
```

## Future Enhancements

### Number Guessing Game
- High score tracking
- Statistics (average attempts, win rate)
- Custom difficulty settings
- Multiplayer mode

### Grade Calculator
- Save/load grade data from files
- Support for multiple classes/semesters
- Grade prediction (what score needed for target grade)
- Export results to CSV/JSON
- Graphical user interface (GUI)

## Author

Created as part of learning Python programming fundamentals.

## License

This project is open source and available for educational purposes.

