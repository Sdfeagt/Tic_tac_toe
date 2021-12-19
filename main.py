# Todo: I'm happy with the current amount of individual functions. Now the plan is to create a "player" function and just call it twice. Code will be way shorter this way.
def borad(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("_____")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("_____")
    print(board[6] + "|" + board[7] + "|" + board[8])


def translate_to_board(cords, board, player):
    if cords == [1, 1]:
        board[6] = player
    if cords == [1, 2]:
        board[3] = player
    if cords == [1, 3]:
        board[0] = player
    if cords == [2, 1]:
        board[7] = player
    if cords == [2, 2]:
        board[4] = player
    if cords == [3, 2]:
        board[5] = player
    if cords == [3, 1]:
        board[8] = player
    if cords == [2, 3]:
        board[1] = player
    if cords == [3, 3]:
        board[2] = player


def diagnoal_win_1(list_of_moves):
    cross = 0
    list_of_moves_internal_use = list_of_moves
    for item_1 in range(0, len(list_of_moves_internal_use)):
        if list_of_moves_internal_use[item_1] == [1, 1]:
            cross = cross + 1
        if list_of_moves_internal_use[item_1] == [2, 2]:
            cross = cross + 1
        if list_of_moves_internal_use[item_1] == [3, 3]:
            cross = cross + 1
    if cross == 3:
        return 1
    else:
        return 0


def diagnoal_win_2(list_of_moves):
    cross = 0
    list_of_moves_internal_use = list_of_moves
    for item_1 in range(0, len(list_of_moves_internal_use)):
        if list_of_moves_internal_use[item_1] == [1, 3]:
            cross = cross + 1
        if list_of_moves_internal_use[item_1] == [2, 2]:
            cross = cross + 1
        if list_of_moves_internal_use[item_1] == [3, 1]:
            cross = cross + 1
    if cross == 3:
        return 1
    else:
        return 0


def main():
    Player_1 = ""
    Player_2 = ""
    x_cord_1 = -1
    y_cord_1 = -1
    x_cord_2 = -2
    y_cord_2 = -2
    win_1 = 0
    win_2 = 0
    list_of_all_moves_1 = []
    list_of_all_moves_2 = []
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    all_moves = 0
    print("Welcome to the tic tac toe game!")

    while Player_1 != "0" and Player_1 != "X":

        Player_1 = input("Player 1, will you play as X or 0? (X/0)\n")

        if Player_1 == "X":
            Player_2 = "0"
        elif Player_1 == "0":
            Player_2 = "X"
        else:
            print("Wrong input! please write 'X' ot '0'!")

    print("Let the game begin! Player 1 will play as {:s}, and Player 2 as {:s}.".format(Player_1, Player_2))
    print("You indicate the place you want to move by using (X,Y) coordinates, with lower left corner as (0,0)")

    borad(board)

    while win_1 != 1 and win_2 != 1 and all_moves != 9:

        while (0 > x_cord_1 or x_cord_1 > 3) and (0 > y_cord_1 or y_cord_1 > 3):
            move_1 = input("Player 1, what's your move?\n")
            move_1 = move_1.split(",")
            x_cord_1 = int(move_1[0])
            y_cord_1 = int(move_1[1])
            if 0 > x_cord_1 or x_cord_1 > 3:
                print("X coordinate is outside of the scope! Repeat the input.\n")
            if 0 > y_cord_1 or y_cord_1 > 3:
                print("Y coordinate is outside of the scope! Repeat the input.\n")
            for item_check_1_1 in range(0, len(list_of_all_moves_1)):
                if list_of_all_moves_1[item_check_1_1] == [x_cord_1, y_cord_1]:
                    print("This field is already taken by another player!")
                    x_cord_1 = -1
                    y_cord_1 = -1
                    break
            for item_check_1_2 in range(0, len(list_of_all_moves_2)):
                if list_of_all_moves_2[item_check_1_2] == [x_cord_1, y_cord_1]:
                    print("This field is already taken by another player!")
                    x_cord_1 = -1
                    y_cord_1 = -1
                    break
        print("Player 1 has chosen a field {},{}! What an exciting move!".format(x_cord_1, y_cord_1))
        list_of_this_cord_1 = [x_cord_1, y_cord_1]
        translate_to_board(list_of_this_cord_1, board, Player_1)
        borad(board)

        list_of_all_moves_1.append(list_of_this_cord_1)
        list_of_all_moves_1.sort(key=lambda x: x[0])

        x_cord_1 = -1
        y_cord_1 = -1

        if len(list_of_all_moves_1) >= 3:
            for i in range(0, len(list_of_all_moves_1) - 2):
                if list_of_all_moves_1[i][0] == list_of_all_moves_1[i + 1][0] == list_of_all_moves_1[i + 2][0]:
                    win_1 = 1
                    print("Player 1 wins!")
                    break
                list_of_all_moves_1.sort(key=lambda x: x[1])
                if list_of_all_moves_1[i][1] == list_of_all_moves_1[i + 1][1] == list_of_all_moves_1[i + 2][1]:
                    win_1 = 1
                    print("Player 1 wins!")
                    break
                list_of_all_moves_1.sort(key=lambda x: x[0])
            diagonal_11 = diagnoal_win_1(list_of_all_moves_1)
            if diagonal_11 == 1:
                print("Player 1 won!")
                break
            diagonal_12 = diagnoal_win_2(list_of_all_moves_1)
            if diagonal_12 == 1:
                print("Player 1 won!")
                break

        all_moves = len(list_of_all_moves_1) + len(list_of_all_moves_2)
        if all_moves == 9 and win_1 != 1:
            print("It's a tie!")
            break

        while (0 > x_cord_2 or x_cord_2 > 3) and (0 > y_cord_2 or y_cord_2 > 3) and win_1 != 1:
            move_2 = input("Player 2, what's your move?\n")
            move_2 = move_2.split(",")
            x_cord_2 = int(move_2[0])
            y_cord_2 = int(move_2[1])
            if 0 > x_cord_2 or x_cord_2 > 3:
                print("X coordinate is outside of the scope! Repeat the input.\n")
            if 0 > y_cord_2 or y_cord_2 > 3:
                print("Y coordinate is outside of the scope! Repeat the input.\n")
            for item_check_2_2 in range(0, len(list_of_all_moves_2)):
                if list_of_all_moves_2[item_check_2_2] == [x_cord_2, y_cord_2]:
                    print("This field is already taken by another player!")
                    x_cord_2 = -1
                    y_cord_2 = -1
                    break
        if win_1 != 1:
            print("Player 2 has chosen a field {},{}! What an exciting move!".format(x_cord_2, y_cord_2))
            list_of_this_cord_2 = [x_cord_2, y_cord_2]
            translate_to_board(list_of_this_cord_2, board, Player_2)
            borad(board)
            list_of_all_moves_2.append(list_of_this_cord_2)
            list_of_all_moves_2.sort(key=lambda x: x[0])

        if len(list_of_all_moves_2) >= 3 and win_1 != 1:
            for j in range(0, len(list_of_all_moves_2) - 2):
                if list_of_all_moves_2[j][0] == list_of_all_moves_2[j + 1][0] == list_of_all_moves_2[j + 2][0]:
                    win_2 = 1
                    print("Player 2 wins!")
                    break
                list_of_all_moves_2.sort(key=lambda x: x[1])
                if list_of_all_moves_2[j][1] == list_of_all_moves_2[j + 1][1] == list_of_all_moves_2[j + 2][1]:
                    win_2 = 1
                    print("Player 2 wins!")
                    break
                list_of_all_moves_2.sort(key=lambda x: x[0])
            diagonal_21 = diagnoal_win_1(list_of_all_moves_2)
            if diagonal_21 == 1:
                print("Player 2 won!")
                break
            diagonal_22 = diagnoal_win_2(list_of_all_moves_2)
            if diagonal_22 == 1:
                print("Player 2 won!")
                break

        x_cord_2 = -2
        y_cord_2 = -2


main()
