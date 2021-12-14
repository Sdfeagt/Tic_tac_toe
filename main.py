from IPython.display import clear_output


# Todo: The program itself runs correctly now. But it lacks excepts for errors and can be simplified. This is what's left to do


def borad(board):
    cl = clear_output()
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("_____")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("_____")
    print(board[6] + "|" + board[7] + "|" + board[8])


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
    cross_1 = 0
    cross_2 = 0
    cross_12 = 0
    cross_22 = 0
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    all_moves = 0
    cant_choose = 0
    cross_1_only_once_1 = 0
    cross_1_only_once_2 = 0
    cross_1_only_once_3 = 0
    cross_2_only_once_1 = 0
    cross_2_only_once_2 = 0
    cross_2_only_once_3 = 0
    cross_12_only_once_1 = 0
    cross_12_only_once_2 = 0
    cross_12_only_once_3 = 0
    cross_21_only_once_1 = 0
    cross_21_only_once_2 = 0
    cross_21_only_once_3 = 0
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
                    cant_choose = 1
                    break
            for item_check_1_2 in range(0, len(list_of_all_moves_2)):
                if list_of_all_moves_2[item_check_1_2] == [x_cord_1, y_cord_1]:
                    print("This field is already taken by another player!")
                    x_cord_1 = -1
                    y_cord_1 = -1
                    cant_choose = 1
                    break
        print("Player 1 has chosen a field {},{}! What an exciting move!".format(x_cord_1, y_cord_1))
        list_of_this_cord_1 = [x_cord_1, y_cord_1]
        if list_of_this_cord_1 == [1, 1]:
            board[6] = Player_1
        if list_of_this_cord_1 == [1, 2]:
            board[3] = Player_1
        if list_of_this_cord_1 == [1, 3]:
            board[0] = Player_1
        if list_of_this_cord_1 == [2, 1]:
            board[7] = Player_1
        if list_of_this_cord_1 == [2, 2]:
            board[4] = Player_1
        if list_of_this_cord_1 == [3, 2]:
            board[5] = Player_1
        if list_of_this_cord_1 == [3, 1]:
            board[8] = Player_1
        if list_of_this_cord_1 == [2, 3]:
            board[1] = Player_1
        if list_of_this_cord_1 == [3, 3]:
            board[2] = Player_1
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
                    print("Debugging. Something wrong with X")
                    break
                elif list_of_all_moves_1[i][1] == list_of_all_moves_1[i + 1][1] == list_of_all_moves_1[i + 2][1]:
                    win_1 = 1
                    print("Player 1 wins!")
                    print("Debugging. Something wrong with Y")
                    break
            for item_1 in range(0, len(list_of_all_moves_1)):
                if list_of_all_moves_1[item_1] == [1, 1] and cross_1_only_once_1 == 0:
                    cross_1 = cross_1 + 1
                    cross_1_only_once_1 = 1
                if list_of_all_moves_1[item_1] == [2, 2] and cross_1_only_once_2 == 0:
                    cross_1 = cross_1 + 1
                    cross_1_only_once_2 = 1
                if list_of_all_moves_1[item_1] == [3, 3] and cross_1_only_once_3 == 0:
                    cross_1 = cross_1 + 1
                    cross_1_only_once_3 = 1
                if cross_1 == 3:
                    win_1 = 1
                    print("Player 1 wins!")
                    print("Debugging. Something wrong with diagonal")
                    break
                if list_of_all_moves_1[item_1] == [1, 3] and cross_2_only_once_1 == 0:
                    cross_2 = cross_2 + 1
                    cross_2_only_once_1 = 1
                if list_of_all_moves_1[item_1] == [2, 2] and cross_2_only_once_2 == 0:
                    cross_2 = cross_2 + 1
                    cross_2_only_once_2 = 1
                if list_of_all_moves_1[item_1] == [3, 1] and cross_2_only_once_3 == 0:
                    cross_2 = cross_2 + 1
                    cross_2_only_once_3 = 1
                if cross_2 == 3:
                    win_1 = 1
                    print("Player 1 wins!")
                    print("Debugging. Something wrong with diagonal")
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
            for item_check_2_1 in range(0, len(list_of_all_moves_1)):
                if list_of_all_moves_1[item_check_2_1] == [x_cord_2, y_cord_2]:
                    print("This field is already taken by another player!")
                    x_cord_2 = -1
                    y_cord_2 = -1
                    break
            for item_check_2_2 in range(0, len(list_of_all_moves_2)):
                if list_of_all_moves_2[item_check_2_2] == [x_cord_2, y_cord_2]:
                    print("This field is already taken by another player!")
                    x_cord_2 = -1
                    y_cord_2 = -1
                    break
        if win_1 != 1:
            print("Player 2 has chosen a field {},{}! What an exciting move!".format(x_cord_2, y_cord_2))
        list_of_this_cord_2 = [x_cord_2, y_cord_2]
        if list_of_this_cord_2 == [1, 1]:
            board[6] = Player_2
        if list_of_this_cord_2 == [1, 2]:
            board[3] = Player_2
        if list_of_this_cord_2 == [1, 3]:
            board[0] = Player_2
        if list_of_this_cord_2 == [2, 1]:
            board[7] = Player_2
        if list_of_this_cord_2 == [2, 2]:
            board[4] = Player_2
        if list_of_this_cord_2 == [3, 2]:
            board[5] = Player_2
        if list_of_this_cord_2 == [3, 1]:
            board[8] = Player_2
        if list_of_this_cord_2 == [2, 3]:
            board[1] = Player_2
        if list_of_this_cord_2 == [3, 3]:
            board[2] = Player_2
        borad(board)
        list_of_all_moves_2.append(list_of_this_cord_2)
        list_of_all_moves_2.sort(key=lambda x: x[0])

        if len(list_of_all_moves_2) >= 3 and win_1 != 1:
            for j in range(0, len(list_of_all_moves_2) - 2):
                if list_of_all_moves_2[j][0] == list_of_all_moves_2[j + 1][0] == list_of_all_moves_2[j + 2][0]:
                    win_2 = 1
                    print("Player 2 wins!")
                    break
                elif list_of_all_moves_2[j][1] == list_of_all_moves_2[j + 1][1] == list_of_all_moves_2[j + 2][1]:
                    win_2 = 1
                    print("Player 2 wins!")
                    break
            for item_2 in range(0, len(list_of_all_moves_2)):
                if list_of_all_moves_2[item_2] == [1, 1] and cross_12_only_once_1 == 0:
                    cross_12 = cross_12 + 1
                    cross_12_only_once_1 = 1
                if list_of_all_moves_2[item_2] == [2, 2] and cross_12_only_once_2 == 0:
                    cross_12 = cross_12 + 1
                    cross_12_only_once_2 = 1
                if list_of_all_moves_2[item_2] == [3, 3] and cross_12_only_once_3 == 0:
                    cross_12 = cross_12 + 1
                    cross_12_only_once_3 = 1
                if cross_12 == 3:
                    win_2 = 1
                    print("Player 2 wins!")
                    break
                if list_of_all_moves_2[item_2] == [1, 3] and cross_21_only_once_1 == 0:
                    cross_22 = cross_22 + 1
                    cross_21_only_once_1 = 1
                if list_of_all_moves_2[item_2] == [2, 2] and cross_21_only_once_2 == 0:
                    cross_22 = cross_22 + 1
                    cross_21_only_once_2 = 1
                if list_of_all_moves_2[item_2] == [1, 3] and cross_21_only_once_3 == 0:
                    cross_22 = cross_22 + 1
                    cross_21_only_once_3 = 1
                if cross_22 == 3:
                    win_2 = 1
                    print("Player 2 wins!")
                    break

        x_cord_2 = -2
        y_cord_2 = -2
        all_moves = len(list_of_all_moves_1) + len(list_of_all_moves_2)

    if all_moves == 9:
        print("It's a tie!")


main()
