def display_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("-----------------------------------------")

def winner(board, n):
    # logic for X player
    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        print(f"Player {n} won the game")
        return True
    if board[0] == "X" and board[3] == "X" and board[6] == "X":
        print(f"Player {n} won the game")
        return True
    if board[0] == "X" and board[4] == "X" and board[8] == "X":
        print(f"Player {n} won the game")
        return True
    if board[6] == "X" and board[4] == "X" and board[2] == "X":
        print(f"Player {n} won the game")
        return True
    if board[6] == "X" and board[7] == "X" and board[8] == "X":
        print(f"Player {n} won the game")
        return True
    if board[3] == "X" and board[4] == "X" and board[5] == "X":
        print(f"Player {n} won the game")
        return True
    if board[1] == "X" and board[4] == "X" and board[7] == "X":
        print(f"Player {n} won the game")
        return True
    if board[2] == "X" and board[5] == "X" and board[8] == "X":
        print(f"Player {n} won the game")
        return True

    # logic for O player
    if board[0] == "O" and board[1] == "O" and board[2] == "O":
        print(f"Player {n} won the game")
        return True
    if board[0] == "O" and board[3] == "O" and board[6] == "O":
        print(f"Player {n} won the game")
        return True
    if board[0] == "O" and board[4] == "O" and board[8] == "O":
        print(f"Player {n} won the game")
        return True
    if board[6] == "O" and board[4] == "O" and board[2] == "O":
        print(f"Player {n} won the game")
        return True
    if board[6] == "O" and board[7] == "O" and board[8] == "O":
        print(f"Player {n} won the game")
        return True
    if board[3] == "O" and board[4] == "O" and board[5] == "O":
        print(f"Player {n} won the game")
        return True
    if board[1] == "O" and board[4] == "O" and board[7] == "O":
        print(f"Player {n} won the game")
        return True
    if board[2] == "O" and board[5] == "O" and board[8] == "O":
        print(f"Player {n} won the game")
        return True
    else:
        return False


board = []
game_on = True
player_1_piece = input("Player 1: Do you want to be an X or an O: ")
player_2_piece = ""
play_again = False
if player_1_piece == "X":
    player_1_piece = "X"
    player_2_piece = "O"
elif player_1_piece == "O":
    player_1_piece = "O"
    player_2_piece = "X"
# have an empty board
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
while(game_on):
    # Player 1 move
    player_1_move = input(f"Player 1: where do you want to place your {player_1_piece} on the board pick a number between 1 and 9: ")
    if not player_1_move.isdigit():
        print("Invalid move pick a number from 1 to 9")
        player_1_move = input(f"Player 1: where do you want to place your {player_1_piece} on the board pick a number between 1 and 9: ")
    else:
        player_1_move_num = int(player_1_move)
        if player_1_move_num < 1 or player_1_move_num > 9:
            print("Invalid move pick a number between 1 to 9")
            player_1_move = input(f"Player 1: where do you want to place your {player_1_piece} on the board pick a number between 1 and 9: ")
        if board[player_1_move_num - 1] == " ":
            board[player_1_move_num - 1] = player_1_piece
        else:
            print("Invalid move \n")
            player_1_move = input(f"Player 1: where do you want to place your {player_1_piece} on the board pick a number between 1 and 9: ")
    
    display_board(board)
    # check if game is over
    if winner(board, "1") == True:
        result = input("Do you want to play again type yes or no: ")
        if result == "yes":
            board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            game_on = True
            continue
        if result == "no":
            print("Thanks for playing")
            break
        

    # Player 2 move
    player_2_move = input(f" Player 2: where do you want to place your {player_2_piece} on the board pick a number between 1 and 9: ")
    if not player_2_move.isdigit():
        print("Invalid move pick a number from 1 to 9")
        input(f" Player 2: where do you want to place your {player_2_piece} on the board pick a number between 1 and 9: ")
    else:
        player_2_move_num = int(player_2_move)
        if player_2_move_num < 1 or player_2_move_num > 9:
            print("Invalid move pick a number between 1 to 9")
            input(f" Player 2: where do you want to place your {player_2_piece} on the board pick a number between 1 and 9: ")
        if board[player_2_move_num - 1] == " ":
            board[player_2_move_num - 1] = player_2_piece
        else:
            print("invalid move")
            input(f" Player 2: where do you want to place your {player_2_piece} on the board pick a number between 1 and 9: ")
    
    display_board(board)
    # check if game is over
    if winner(board, "2") == True:
        result = input("Do you want to play again type yes or no: ")
        if result == "yes":
            board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        if result == "no":
            print("Thanks for playing")
            break

    








