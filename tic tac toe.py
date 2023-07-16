# Function to print the tic-tac-toe board
def print_tic_t_t(values):
    print("\n")
    print("  {}  |  {}  |  {}  ".format(values[0], values[1], values[2]))
    print(" ----|-----|----")
    print("  {}  |  {}  |  {}  ".format(values[3], values[4], values[5]))
    print(" ----|-----|----")
    print("  {}  |  {}  |  {}  ".format(values[6], values[7], values[8]))
    print("\n")

# Function to create the scoreboard for the game
def print_ScoreBoard(Score_Board):
    print("----------SCORE BOARD FOR TIC TAC TOE GAME----------")
    players = list(Score_Board.keys())
    print(" \t ", players[0], " \t ", Score_Board[players[0]])
    print(" \t ", players[1], " \t ", Score_Board[players[1]])
    print("\t----------------------------------------------------")

# Function to check if any player has won the match
def check_winner(player_position, current_player):
    # All possible winning combinations for the players
    combination = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    
    # Loop to check if any combinations satisfy or not
    for x in combination:
        if all(y in player_position[current_player] for y in x):
            # Return True if any winning combination is satisfied in iteration
            return True

    # Return False if no winning combination is satisfied
    return False

# Function to check if the game is a draw
def check_draw(player_position):
    if len(player_position['X']) + len(player_position['O']) == 9:
        return True
    return False

# Function for a single Tic-tac-toe game
def single_game(current_player):
    # Represent the tic-tac-toe
    values = [' ' for _ in range(9)]
    # Store the position occupied by X and O
    player_position = {'X': [], 'O': []}
    
    # Game loop for a single game of tic-tac-toe
    while True:
        print_tic_t_t(values)
        
        # Try-except block for move input
        try:
            print("Player", current_player, "turn. Which box?:", end=" ")
            move = int(input())
        except ValueError:
            print("Wrong Input!!!!! TRY AGAIN :)")
            continue

        # Check for move in or out
        if move < 1 or move > 9:
            print("Please choose the right number between 1 to 9")
            continue

        # Check if the cell is occupied or not
        if values[move - 1] != ' ':
            print("The place you have chosen is not free.......try again")
            continue

        # Logic for updating the board status
        values[move - 1] = current_player

        # Updating player position
        player_position[current_player].append(move)

        # Function call for checking the winner
        if check_winner(player_position, current_player):
            print_tic_t_t(values)
            print("Player", current_player, "has won the game!!")
            print("\n")
            return current_player

        # Function call for checking draw game
        if check_draw(player_position):
            print_tic_t_t(values)
            print("AWWW NO ONE WON THE GAME, IT'S A TIE")
            return 'D'

        # Switch player moves
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

if __name__ == "__main__":
    print("Player 1 details")
    play1 = input("Enter the name of player: ")
    print("\n")
    print("Player 2 details")
    play2 = input("Enter the name of player: ")
    print("\n")
    
    # Store the player who chooses X or O
    current_player = play1
    # Store the choice of player character
    player_choice = {'X': " ", 'O': " "}
    # Store the options
    options = ['X', 'O']
    # Store the scoreboard details
    Score_Board = {play1: 0, play2: 0}
    
    print_ScoreBoard(Score_Board)

    # The loop runs until either of the players choose to quit
    while True:
        # Player choice menu
        print("Turn to choose for", current_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to quit")

        # Try-except for CHOICE input
        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue

        # Condition for player choice
        if choice == 1:
            player_choice['X'] = current_player
            if current_player == play1:
                player_choice['O'] = play2
            else:
                player_choice['O'] = play1
        elif choice == 2:
            player_choice['O'] = current_player
            if current_player == play1:
                player_choice['X'] = play2
            else:
                player_choice['X'] = play1
        elif choice == 3:
            print("Final Scores")
            print_ScoreBoard(Score_Board)
            break
        else:
            print("Wrong choice. Try again")

        # Store the winner in a single game of tic-tac-toe
        winner = single_game(options[choice - 1])

        # Scoreboard edits according to the winner
        if winner != 'D':
            player_won = player_choice[winner]
            Score_Board[player_won] = Score_Board[player_won] + 1

        print_ScoreBoard(Score_Board)

        # Switch player who chooses X or O
        if current_player == play1:
            current_player = play2
        else:
            current_player = play1
