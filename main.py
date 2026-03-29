"""
Tic-Tac-Toe (2-player console game)

This module implements a simple 2-player Tic-Tac-Toe game playable in the console.
No external dependencies are required beyond the standard library.

How to run:
- Execute this file with Python 3.6+:
    python main.py
- The program will prompt for player names and markers, then run games until players quit.

Notes for maintainers:
- The board is represented by a list `grid` of length 9. Indices 0..8 correspond to positions 1..9 shown to users.
- Players are represented as [name, marker]. Example: player_1 = ["ALICE", "X"]
- The code uses simple input validation and prints colored errors using ANSI escape codes.
"""

from time import sleep

# __ASCII ART__

title_logo = r"""
$$$$$$$$\ $$$$$$\  $$$$$$\ $$$$$$$$\  $$$$$$\   $$$$$$\ $$$$$$$$\  $$$$$$\  $$$$$$$$\
\__$$  __|\_$$  _|$$  __$$\\__$$  __|$$  __$$\ $$  __$$\\__$$  __|$$  __$$\ $$  _____|
   $$ |     $$ |  $$ /  \__|  $$ |   $$ /  $$ |$$ /  \__|  $$ |   $$ /  $$ |$$ |
   $$ |     $$ |  $$ |$$$$$$\ $$ |   $$$$$$$$ |$$ |$$$$$$\ $$ |   $$ |  $$ |$$$$$\
   $$ |     $$ |  $$ |\______|$$ |   $$  __$$ |$$ |\______|$$ |   $$ |  $$ |$$  __|
   $$ |     $$ |  $$ |  $$\   $$ |   $$ |  $$ |$$ |  $$\   $$ |   $$ |  $$ |$$ |
   $$ |   $$$$$$\ \$$$$$$  |  $$ |   $$ |  $$ |\$$$$$$  |  $$ |    $$$$$$  |$$$$$$$$\
   \__|   \______| \______/   \__|   \__|  \__| \______/   \__|    \______/ \________|
                                                                                      """

# __HELPER FUNCTIONS__

def print_error(msg):
    """
    Print an error message in red color for better visibility.

    Args:
        msg (str): The error message to display.
    """
    # ANSI escape code \033[91m sets red text, \033[0m resets color.
    print(f"\033[91m{msg}\033[0m")


def get_valid_name(prompt):
    """
    Prompt repeatedly until a non-empty, non-whitespace name is provided.

    Args:
        prompt (str): The prompt to show to the user.

    Returns:
        str: The entered name (trimmed).
    """
    while True:
        name = input(prompt).strip()  # remove surrounding whitespace
        if not name:
            # Inform the user and prompt again
            print_error("Name cannot be blank or only whitespace. PLEASE ENTER A VALID NAME.\n")
            continue
        return name


def win_check():
    """
    Check the current grid for a winning combination.

    Returns:
        str|bool: The winning player's name if a win is detected, otherwise False.

    Notes:
        - Uses the player markers to decide winner name.
        - Expects global variables: grid, player_1_marker, player_2_marker, player_1_name, player_2_name.
    """
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]

    for combo in winning_combinations:
        a, b, c = combo

        if grid[a] == grid[b] == grid[c] and grid[a] != " ":
            # determine which player won based on marker
            if grid[a] == player_1_marker:
                return player_1_name
            else:
                return player_2_name

    return False


def draw_check():
    """
    Check if the game is a draw (no empty spaces and no winner).

    Returns:
        bool: True if draw, False otherwise.
    """
    # If there is no space in grid and win_check() returned False, it's a draw.
    if " " not in grid and win_check() == False:
        return True
    else:
        return False


def display_grid():
    """
    Print the current grid state in a user-friendly 3x3 format.

    Example:
     X | O | X
    ---+---+---
     O | X | O
    """
    print(f"\nCurrent Grid State:\n"
          f" {grid[0]} | {grid[1]} | {grid[2]} \n"
          f"---+---+---\n"
          f" {grid[3]} | {grid[4]} | {grid[5]} \n"
          f"---+---+---\n"
          f" {grid[6]} | {grid[7]} | {grid[8]} \n")


def display_positions():
    """
    Display the numeric reference for grid positions so users know which number maps to which cell.
    """
    print("\nGrid Position Reference:\n"
          " 1 | 2 | 3 \n"
          "---+---+---\n"
          " 4 | 5 | 6 \n"
          "---+---+---\n"
          " 7 | 8 | 9 \n")


def display_rules():
    """
    Show the game rules to the players with small delays to improve readability.

    This function uses sleep() to pace the output for new players.
    """
    print("\n===== GAME RULES =====\n")
    sleep(2)
    print("1. This is a 2-player Tic Tac Toe game.")
    sleep(1)
    print("2. Players will take turns placing their marker (X or O) on the grid.")
    sleep(1)
    print("3. The grid positions are numbered from 1 to 9 as follows:")
    display_positions()
    sleep(1)
    print("4. On your turn, enter a number (1-9) to place your marker.")
    sleep(1)
    print("5. You cannot place your marker on an already occupied position.")
    sleep(1)
    print("6. The first player to get 3 markers in a row (horizontal, vertical, or diagonal) wins.")
    sleep(1)
    print("7. If all positions are filled and no one wins, the game ends in a draw.")
    sleep(1)
    print("\nLet the game begin!\n")


def get_valid_move(current_player):
    """
    Ask the current player for a move, validate it, and update the grid.

    Args:
        current_player (list): [player_name, marker]

    Returns:
        list: The next current_player (player_1 or player_2).
    """
    valid_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while True:
        # Prompt shows player's initial and their marker to avoid confusion.
        user_input = input(f"\n{current_player[0]}, please enter the number corresponding to the grid position where you want to place your marker '{current_player[1]}'.\n-> ").strip()

        if not user_input.isdigit():
            print_error("Invalid input. Please enter a number between 1 and 9.")
            sleep(1)
            continue

        player_move = int(user_input)

        if player_move not in valid_moves:
            print_error("Invalid input. Enter a number from 1 to 9.")
            sleep(1)
            continue

        # Check if chosen cell is empty
        if grid[player_move - 1] != " ":
            print_error("That position is already occupied. Please choose an empty position.")
            sleep(1)
            continue

        # Place the marker on the board (side-effect on global `grid`)
        grid[player_move - 1] = current_player[1]

        # Switch current player by comparing lists (works because we store exact references below)
        current_player = player_2 if current_player == player_1 else player_1
        return current_player


def play_game(current_player):
    """
    Main routine for playing a single match until there is a win or a draw.

    Args:
        current_player (list): The player who will move first in this game.

    Returns:
        bool: False when the match finishes (used by caller to trigger replay prompt).
    """
    while True:
        print(f"{current_player[0]}'s turn. Your marker is '{current_player[1]}'.")
        display_positions()  # help players remember numeric layout
        display_grid()
        current_player = get_valid_move(current_player=current_player)
        if win_check():
            display_grid()
            print(f"Congratulations {win_check()}! You have won the game!")
            return False
        elif draw_check():
            display_grid()
            print("The game is a draw! No more moves left and no winner.")
            return False
        else:
            # Continue to next turn
            continue


# __WELCOME MESSAGE__

print(title_logo)
print("WELCOME TO THE 2 PLAYER GAME OF TIC TAC TOE. \nHOPE, YOU HAVE BROUGHT YOU FRIEND ALONG.\n\nENJOY YOUR TIME!! ")

# __GRID SETUP__
# The board state: list of 9 positions. " " means empty.
grid = [" " for _ in range(9)]

# __PLAYER SETUP__
print("\nPlease enter names of both the players:")

# Ask for player names and normalize to uppercase for consistent display
player_1_name = get_valid_name("Player 1 Name\n-> ").upper()
player_2_name = get_valid_name("Player 2 Name\n-> ").upper()
player_1_marker = ""
player_2_marker = ""

wrong_answer_1 = True

# Loop until player 1 chooses either 'X' or 'O' (case-insensitive)
while wrong_answer_1 == True:
    # Trim whitespace and uppercase for comparison
    player_1_marker = input(f"What shall {player_1_name}'s marker be? It can either be 'X' or 'O'.\n-> ").strip().upper()
    # Validate using membership check similar to player 2's validation
    if player_1_marker not in ('X', 'O'):
        print_error(f"{player_1_name}'s marker can only be 'O' or 'X' \nPLEASE CHOOSE AGAIN.\n")
        wrong_answer_1 = True
    else:
        # Assign the opposite marker to player 2
        print(f"{player_1_name}'s marker will be '{player_1_marker}'.\n"
              f"Therefore, {player_2_name} will be assigned '{'O' if player_1_marker == 'X' else 'X'}' as their marker.\n")
        player_2_marker = 'O' if player_1_marker == 'X' else 'X'
        wrong_answer_1 = False
        sleep(3)

# Players are simple lists [name, marker] used throughout the code
player_1 = [player_1_name, player_1_marker]
player_2 = [player_2_name, player_2_marker]

# The player who starts the match
current_player = player_1

# __GAME LOOP__
# Outer loop managing multiple matches until players decide to quit.
game_over = False

while not game_over:
    display_rules()  # show rules at start of each match
    sleep(3)
    if not play_game(current_player=current_player):
        # When a match finishes, ask players if they would like to play again.
        while True:
            continue_game = input("Would you like to play again? (Y/N)\n-> ").strip().upper()
            if continue_game == "Y":
                # Reset board state and keep same starting player
                game_over = False
                grid = [" " for _ in range(9)]
                break
            elif continue_game == "N":
                print("Well, it's your choice after all. Good game.\nTHANK YOU.")
                game_over = True
                break
            else:
                print_error("Invalid input. Please enter 'Y' or 'N'.\n")
