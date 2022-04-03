'''
Don't Get Volunteered!
======================

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and ordering the bunnies around at the same time, after all! In order to make sure that everyone is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution(0, 1)
Output:
    3

Input:
solution.solution(19, 36)
Output:
    1

-- Java cases --
Input:
Solution.solution(19, 36)
Output:
    1

Input:
Solution.solution(0, 1)
Output:
    3'''
from test import *

def solution(src, dest):
    
    # Create a board
    height = 8
    width = 8
    board = []
    starting_coordinate = ''
    target_coordinate = ''

    x = 0
    while x < width:
        y = 0
        while y < height:
            coordinate = [x,y]
            square = {'coordinate' : coordinate, 'starting' : False, 'target' : False}
            board.append(square)
            y += 1
        x += 1

    # Set the starting piece:
    counter = 0
    for square in board:
        if counter == src:
            board[counter]['starting'] = True
            starting_coordinate = board[counter]['coordinate']
        counter += 1

    # Set the target piece:
    counter = 0
    for square in board:
        if counter == dest:
            board[counter]['target'] = True
            target_coordinate = board[counter]['coordinate']
        counter += 1

    if starting_coordinate == target_coordinate:
        return 0

    # Move directions for our knight
    moves = [[-1,-2], [-1,2], [1,-2], [1,2], [2,-1], [2,1], [-2,1], [-2,-1]]

    # Finding possible squares for the knight to move to
    layers = 1
    starting_moves = [starting_coordinate]
    found_moves = []
    skip = False
    moved_to_spaces = []

    while True:
        # Storing every move a piece can move to 
        found_moves = []
        for position in starting_moves:
            x = position[0]
            y = position[1]

            for move in moves:
                x1 = move[0]
                y1 = move[1]
                new_location = [abs(x+x1), abs(y+y1)]

                # If the a move to that square hasn't occurred yet
                if new_location not in moved_to_spaces:
                    # If the move is off the board, do not add it
                    for axis in new_location:
                        if axis > 7:
                            skip = True
                    if skip == True:
                        skip = False
                        continue

                    # If the move is legal, add it to list of locations
                    found_moves.append(new_location)
                    moved_to_spaces.append(new_location)


        # Set the lists for next iteration
        starting_moves = found_moves
        if target_coordinate in found_moves:
            return layers
            
        layers += 1

# Create a board
height = 8
width = 8
board = []
starting_coordinate = ''
target_coordinate = ''       
x = 0
while x < width:
    y = 0
    while y < height:
        coordinate = [x,y]
        square = {'coordinate' : coordinate, 'starting' : False, 'target' : False}
        board.append(square)
        y += 1
    x += 1
    


answers1 = []
answers2 = []
for number1 in range(0,63):
    for number2 in range(0,63):
            answer1 = solution(number1,number2)
            answers1.append(answer1)

            answer2 = minStepToReachTarget(board[number1]['coordinate'], board[number2]['coordinate'], 8)
            answers2.append(answer2)
            if answer1 != answer2:
                print board[number1]['coordinate'], board[number2]['coordinate']
                print answer1, answer2
