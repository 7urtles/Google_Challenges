'''
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

Write a function solution(map) that generates the length of the shortest path from the station door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

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
solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
Output:
    7

Input:
solution.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
Output:
    11

-- Java cases -- 
Input:
Solution.solution({{0, 1, 1, 0}, {0, 0, 0, 1}, {1, 1, 0, 0}, {1, 1, 1, 0}})
Output:
    7

Input:
Solution.solution({{0, 0, 0, 0, 0, 0}, {1, 1, 1, 1, 1, 0}, {0, 0, 0, 0, 0, 0}, {0, 1, 1, 1, 1, 1}, {0, 1, 1, 1, 1, 1}, {0, 0, 0, 0, 0, 0}})
Output:
    11
'''
from tools import display, map_maker
from maze import *
from itertools import count
floor_plan =  [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]


# Maze
floor_plan = maze().make_maze()
# Random walls
# floor_plan = map_maker()


def solution(floor_plan):
    # Setting the height and width (Intentionally not reducing the lenght by 1)
    height = len(floor_plan)
    width = len(floor_plan[0])

    # Make the blueprint of the floor a tuple to stop accidental value changes due to memory pointers
    floor_plan = tuple([tuple(row) for row in floor_plan])
    turns_taken = [10000]
    # For the starting space coordinate decrementing by one is necessary
    starting_space = (width-1, height-1)
    move_directions = ((0,-1), (0,1), (1,0), (-1,0))
    
    
    # Checking all spaces for a wall
    for yaxis in range(0,height): # Every row in the map
        for xaxis in range(0,width): # Every space in the row
            # Placing the search algorithm starting square
            searchers = [starting_space]
            # Initialized with a value of 1, placing our starting space counts as a move
            moves_taken = 1
            # Create an editable copy of the floor plan
            floor_plan_copy = [list(row) for row in floor_plan]
            # If the space has a wall on it
            if floor_plan[yaxis][xaxis] == 1:
            
                # Remove the wall for the current iteration
                floor_plan_copy[yaxis][xaxis] = 0
                # While the goal is not found, and there are possible moves 
                while True:
                    # Holds spaces to search from on the next iteration
                    new_searchers = []
                    # For every active search node
                    for searcher in searchers:
                        # Check the spaces around it
                        for move in move_directions:
                            # Looking over the edges causes index errors, try/except to avoid those moments
                            try:
                                # BUG searchers can look around to the opposite end of their row if on an edge....
                                if searcher[1]+move[1] == -1 or searcher[0]+move[0] == -1:
                                    continue
                                # If the space around its not a wall, or has not been infected
                                if floor_plan_copy[searcher[1]+move[1]][searcher[0]+move[0]] != 1 and floor_plan_copy[searcher[1]+move[1]][searcher[0]+move[0]] != 99:
                                    # Infect that space
                                    floor_plan_copy[searcher[1]+move[1]][searcher[0]+move[0]] = 99
                                    # Spread a searcher to that location for next movement cycle
                                    new_searchers.append((searcher[0]+move[0],searcher[1]+move[1]))
                            
                            except:
                                # Uh oh.. Looked over the edge and fell off                    
                                pass

                    
                    # Make a tuple of searchers consisting of all infected positions from the iteration
                    searchers = tuple(new_searchers)
                    # Increase number of moves taken so far
                    moves_taken += 1
                    # If the searcher found the goal
                    if floor_plan_copy[0][0] == 99:
                        # Remember how many moves it took to get there
                        turns_taken.append(moves_taken)
                        # Time to start over
                        break
                    # If there is no where to move
                    if len(searchers) == 0:
                        # Start the search over with a different wall removed
                        break

                    # For visualizing data
                    # display(floor_plan_copy)
    
    return min(turns_taken)




print(solution(floor_plan))