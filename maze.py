# self.maze generator -- Randomized Prim Algorithm

## Imports
import random
class maze:
    def __init__(self):
        ## Main code
        # Init variables
        self.wall = 1
        self.cell = 0
        self.unvisited = 'u'
        self.height = 1000
        self.width = 1000
        

    def make_maze(self):
        self.maze = []

        # Denote all cells as self.unvisited
        for i in range(0, self.height):
            # line = []
            line = [self.unvisited for item in range(self.width)]
            # for j in range(0, self.width):
            #     line.append(self.unvisited)
            self.maze.append(line)

        # Randomize starting point and set it a self.cell
        starting_height = int(random.random()*self.height)
        starting_width = int(random.random()*self.width)
        if (starting_height == 0):
            starting_height += 1
        if (starting_height == self.height-1):
            starting_height -= 1
        if (starting_width == 0):
            starting_width += 1
        if (starting_width == self.width-1):
            starting_width -= 1

        # Mark it as self.cell and add surrounding self.walls to the list
        self.maze[starting_height][starting_width] = self.cell
        self.walls = []
        self.walls.append([starting_height - 1, starting_width])
        self.walls.append([starting_height, starting_width - 1])
        self.walls.append([starting_height, starting_width + 1])
        self.walls.append([starting_height + 1, starting_width])

        # Denote self.walls in self.maze
        self.maze[starting_height-1][starting_width] = 1
        self.maze[starting_height][starting_width - 1] = 1
        self.maze[starting_height][starting_width + 1] = 1
        self.maze[starting_height + 1][starting_width] = 1

        while (self.walls):
            # Pick a random self.wall
            rand_wall = self.walls[int(random.random()*len(self.walls))-1]

            # Check if it is a left self.wall
            if (rand_wall[1] != 0):
                if (self.maze[rand_wall[0]][rand_wall[1]-1] == 'u' and self.maze[rand_wall[0]][rand_wall[1]+1] == 0):
                    # Find the number of surrounding cells
                    s_cells = self.surroundingCells(rand_wall)

                    if (s_cells < 2):
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = 0

                        # Mark the new self.walls
                        # Upper self.cell
                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0]-1][rand_wall[1]] != 0):
                                self.maze[rand_wall[0]-1][rand_wall[1]] = 1
                            if ([rand_wall[0]-1, rand_wall[1]] not in self.walls):
                                self.walls.append([rand_wall[0]-1, rand_wall[1]])


                        # Bottom self.cell
                        if (rand_wall[0] != self.height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]] != 0):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = 1
                            if ([rand_wall[0]+1, rand_wall[1]] not in self.walls):
                                self.walls.append([rand_wall[0]+1, rand_wall[1]])

                        # Leftmost self.cell
                        if (rand_wall[1] != 0):	
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] != 0):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = 1
                            if ([rand_wall[0], rand_wall[1]-1] not in self.walls):
                                self.walls.append([rand_wall[0], rand_wall[1]-1])
                    

                    # Delete self.wall
                    for self.wall in self.walls:
                        if (self.wall[0] == rand_wall[0] and self.wall[1] == rand_wall[1]):
                            self.walls.remove(self.wall)

                    continue

            # Check if it is an upper self.wall
            if (rand_wall[0] != 0):
                if (self.maze[rand_wall[0]-1][rand_wall[1]] == 'u' and self.maze[rand_wall[0]+1][rand_wall[1]] == 0):

                    s_cells = self.surroundingCells(rand_wall)
                    if (s_cells < 2):
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = 0

                        # Mark the new self.walls
                        # Upper self.cell
                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0]-1][rand_wall[1]] != 0):
                                self.maze[rand_wall[0]-1][rand_wall[1]] = 1
                            if ([rand_wall[0]-1, rand_wall[1]] not in self.walls):
                                self.walls.append([rand_wall[0]-1, rand_wall[1]])

                        # Leftmost self.cell
                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] != 0):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = 1
                            if ([rand_wall[0], rand_wall[1]-1] not in self.walls):
                                self.walls.append([rand_wall[0], rand_wall[1]-1])

                        # Rightmost self.cell
                        if (rand_wall[1] != self.width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1] != 0):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = 1
                            if ([rand_wall[0], rand_wall[1]+1] not in self.walls):
                                self.walls.append([rand_wall[0], rand_wall[1]+1])

                    # Delete self.wall
                    for self.wall in self.walls:
                        if (self.wall[0] == rand_wall[0] and self.wall[1] == rand_wall[1]):
                            self.walls.remove(self.wall)

                    continue

            # Check the bottom self.wall
            if (rand_wall[0] != self.height-1):
                if (self.maze[rand_wall[0]+1][rand_wall[1]] == 'u' and self.maze[rand_wall[0]-1][rand_wall[1]] == 0):

                    s_cells = self.surroundingCells(rand_wall)
                    if (s_cells < 2):
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = 0

                        # Mark the new self.walls
                        if (rand_wall[0] != self.height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]] != 0):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = 1
                            if ([rand_wall[0]+1, rand_wall[1]] not in self.walls):
                                self.walls.append([rand_wall[0]+1, rand_wall[1]])
                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] != 0):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = 1
                            if ([rand_wall[0], rand_wall[1]-1] not in self.walls):
                                self.walls.append([rand_wall[0], rand_wall[1]-1])
                        if (rand_wall[1] != self.width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1] != 0):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = 1
                            if ([rand_wall[0], rand_wall[1]+1] not in self.walls):
                                self.walls.append([rand_wall[0], rand_wall[1]+1])

                    # Delete self.wall
                    for self.wall in self.walls:
                        if (self.wall[0] == rand_wall[0] and self.wall[1] == rand_wall[1]):
                            self.walls.remove(self.wall)


                    continue

            # Check the right self.wall
            if (rand_wall[1] != self.width-1):
                if (self.maze[rand_wall[0]][rand_wall[1]+1] == 'u' and self.maze[rand_wall[0]][rand_wall[1]-1] == 0):

                    s_cells = self.surroundingCells(rand_wall)
                    if (s_cells < 2):
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = 0

                        # Mark the new self.walls
                        if (rand_wall[1] != self.width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1] != 0):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = 1
                            if ([rand_wall[0], rand_wall[1]+1] not in self.walls):
                                self.walls.append([rand_wall[0], rand_wall[1]+1])
                        if (rand_wall[0] != self.height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]] != 0):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = 1
                            if ([rand_wall[0]+1, rand_wall[1]] not in self.walls):
                                self.walls.append([rand_wall[0]+1, rand_wall[1]])
                        if (rand_wall[0] != 0):	
                            if (self.maze[rand_wall[0]-1][rand_wall[1]] != 0):
                                self.maze[rand_wall[0]-1][rand_wall[1]] = 1
                            if ([rand_wall[0]-1, rand_wall[1]] not in self.walls):
                                self.walls.append([rand_wall[0]-1, rand_wall[1]])

                    # Delete self.wall
                    for self.wall in self.walls:
                        if (self.wall[0] == rand_wall[0] and self.wall[1] == rand_wall[1]):
                            self.walls.remove(self.wall)

                    continue

            # Delete the self.wall from the list anyway
            [self.walls.remove(self.wall) for self.wall in self.walls if (self.wall[0] == rand_wall[0] and self.wall[1] == rand_wall[1])]
            # for self.wall in self.walls:
            #     if (self.wall[0] == rand_wall[0] and self.wall[1] == rand_wall[1]):
            #         self.walls.remove(self.wall)
            


        # Mark the remaining self.unvisited cells as self.walls
        for i in range(0, self.height):
            for j in range(0, self.width):
                if (self.maze[i][j] == 'u'):
                    self.maze[i][j] = 1

        # Set entrance and exit
        for i in range(0, self.width):
            if (self.maze[1][i] == 0):
                self.maze[0][i] = 0
                break

        for i in range(self.width-1, 0, -1):
            if (self.maze[self.height-2][i] == 0):
                self.maze[self.height-1][i] = 0
                break
        self.maze[0][0] = 0
        print('Maze Generated')
        return self.maze

    # Find number of surrounding cells
    def surroundingCells(self,rand_wall):
        s_cells = 0
        if (self.maze[rand_wall[0]-1][rand_wall[1]] == 0):
            s_cells += 1
        if (self.maze[rand_wall[0]+1][rand_wall[1]] == 0):
            s_cells += 1
        if (self.maze[rand_wall[0]][rand_wall[1]-1] == 0):
            s_cells +=1
        if (self.maze[rand_wall[0]][rand_wall[1]+1] == 0):
            s_cells += 1

        return s_cells

