row = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
choices = {
    1: row[0],
    2: row[1],
    3: row[2],
    4: row[3],
    5: row[4],
    6: row[5],
    7: row[6],
    8: row[7],
    9: row[8],
}
turn = 0
player1 = "x"
player2 = "o"


def print_board():
    """Print out the board for the game"""
    print(f"{row[6]} | {row[7]} | {row[8]}")
    print("----------")
    print(f"{row[3]} | {row[4]} | {row[5]}")
    print("----------")
    print(f"{row[0]} | {row[1]} | {row[2]}")


def active_player(turn):
    """Checks the active player"""
    if turn % 2 == 0:
        return player2
    else:
        return player1


def user_turn():
    """Takes input from the player and checks if the spot is available to place on the board"""
    global turn
    try:
        user_choice = int(input("Enter Option: "))
    except ValueError:
        print("Please make a valid choice")
        turn -= 1
    else:
        try:
            if row[user_choice - 1] == " ":
                row[user_choice - 1] = row[user_choice - 1].replace(" ", player)
            else:
                print("Space already taken")
                turn -= 1
        except IndexError:
            print("Please select a number between 1-9")
            turn -= 1


def check_win(player):
    """Check if there is a winning combination"""
    if (
            row[0] == row[1] == row[2] == player
            or row[3] == row[4] == row[5] == player
            or row[6] == row[7] == row[8] == player
            or row[0] == row[3] == row[6] == player
            or row[1] == row[4] == row[7] == player
            or row[2] == row[5] == row[8] == player
            or row[0] == row[4] == row[8] == player
            or row[2] == row[4] == row[6] == player):
        return True


if __name__ == "__main__":
    while True:
        if " " in row:
            turn += 1
            player = active_player(turn)
            print_board()
            user_turn()
            if check_win(player):
                print_board()
                print(f"{player} wins!!!!")
                break
        else:
            print_board()
            print("Draw!!!")
            break
    print("Game Over!")
