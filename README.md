Hello, and welcome to my very first project! This program was created to test my skills I acquired
in my first python programming course. I was able to create most of the code in 2 days, but I've spent some more time creating functions, and cleaning the code. I'm overall very happy with the code
I've created. The program itself is located in one file, main.py. It's made out of 5 functions, excluding main.

board_function is responsible for outputting the current board, with all previous moves of players. This function gets a 9 index long list, filled with corresponding player moves, or just spaces.
Every time this function is called, it prints a board.

translate_to_board is one of the most important functions in my code. It's responsible for creating board lists, used in board_function. Every move given by a user is translated into a proper index
in the list, which makes creating the board much easier.

diagonal_win_1 and diagonal_win_2 are very similar as they check whether a given player has placed their moves in a way that guarantees a diagonal win. It runs by all moves the player did
looking for a proper pattern, which is different for those functions.

 random_text is the least necessary function in this code. It simply makes the output a bit more interesting, and the game more exciting!
 
 I welcome you to check out the code itself, you're naturally free to use it as per the licensing agreement.
