# Tic-Tac-Toe — 2‑player console game

A small, dependency-free Tic-Tac-Toe game for two players that runs in the terminal.  
Designed for clarity and easy modification.

## Features
- Input validation (invalid, out-of-range, occupied cells)
- Colored error messages using ANSI escape codes
- Replay system to play multiple matches without restarting
- Clean, focused functions to keep logic readable and easy to refactor

## Overview
Players enter names and choose markers (X or O). The game validates input, displays the board, detects wins/draws, and prompts to replay. No external packages required.

## Prerequisites
- Python 3.6 or newer

## How to run
1. Open a terminal.
2. Change to the project folder:
```bash
cd path/to/project-folder
```
3. Run the game:
```bash
python main.py
```

## Gameplay
- Player 1 chooses a marker (X or O); Player 2 receives the opposite marker.
- Positions on the board are numbered 1–9 as shown:
```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```
- On your turn, enter the number of an empty position to place your marker.
- The game detects a win (three in a row) or a draw (board full with no winner) and then asks whether to play again.

## Project structure
- `main.py` — main game program and all game logic

## Developer notes (quick reference)
- Board
  - `grid`: list of 9 strings; each entry is `" "` or a marker `'X'`/`'O'`. Index 0 maps to position 1.
- Players
  - `player_1` / `player_2`: lists in the form `[name, marker]`
  - `current_player`: reference to the player whose turn it is
- Key functions
  - `get_valid_name(prompt)` — prompt until a non-empty name is provided
  - `get_valid_move(current_player)` — validate and apply a player's move; updates `grid`
  - `display_grid()` / `display_positions()` — print current board and numeric reference
  - `win_check()` — returns the winning player's name or False
  - `draw_check()` — returns True when board is full with no winner
  - `play_game(current_player)` — play a single match until win/draw

## Contributing / Extending
Suggestions for improvement:
- Split logic into modules (e.g., board.py, players.py) to enable unit testing
- Add an AI opponent mode
- Add a test suite for `win_check()` and `draw_check()`

## Testing
- Manual: run a few matches and exercise invalid inputs (non-digit, out-of-range, occupied cell) to verify behavior.
- Automated: after refactor, add unit tests for board logic and input handling.