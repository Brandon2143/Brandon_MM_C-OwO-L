from API import *
import sys

#JOE's MAMA birthed JOE to help me create this

class mazeCell():
    
    n = False
    s = False
    e = False
    w = False

    def __init__(self, initalValue=255):
        self.value = initalValue

valueMap = [
    [14, 13, 12, 11, 10, 9, 8, 7, 7, 8, 9, 10, 11, 12, 13, 14],
    [13, 12, 11, 10, 9, 8, 7, 6, 6, 7, 8, 9, 10, 11, 12, 13],
    [12, 11, 10, 9, 8, 7, 6, 5, 5, 6, 7, 8, 9, 10, 11, 12],
    [11, 10, 9, 8, 7, 6, 5, 4, 4, 5, 6, 7, 8, 9, 10, 11],
    [10, 9, 8, 7, 6, 5, 4, 3, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 8, 7, 6, 5, 4, 3, 2, 2, 3, 4, 5, 6, 7, 8, 9],
    [8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8],
    [7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7],
    [7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7],
    [8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8],
    [9, 8, 7, 6, 5, 4, 3, 2, 2, 3, 4, 5, 6, 7, 8, 9],
    [10, 9, 8, 7, 6, 5, 4, 3, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 10, 9, 8, 7, 6, 5, 4, 4, 5, 6, 7, 8, 9, 10, 11],
    [12, 11, 10, 9, 8, 7, 6, 5, 5, 6, 7, 8, 9, 10, 11, 12],
    [13, 12, 11, 10, 9, 8, 7, 6, 6, 7, 8, 9, 10, 11, 12, 13],
    [14, 13, 12, 11, 10, 9, 8, 7, 7, 8, 9, 10, 11, 12, 13, 14],
]

#sets up the matrix and assigns a value, a boolean for walls, and a position 

maze = []
for y in range(16):
    row = []
    for x in range(16):
        row.append(mazeCell(valueMap[x][y]))
    maze.append(row)

# Constants for maze directions
MAZE_NORTH = 'n'
MAZE_EAST = 'e'
MAZE_SOUTH = 's'
MAZE_WEST = 'w'


# Function to update the micromouse orientation based on its movement, def did not get inspire by the holy grail of Chat GPT
def update_MO(T_D):
    global MO
    if T_D == 'Right':
        if MO == MAZE_NORTH:
            MO = MAZE_EAST
        elif MO == MAZE_EAST:
            MO = MAZE_SOUTH
        elif MO == MAZE_SOUTH:
            MO = MAZE_WEST
        elif MO == MAZE_WEST:
            MO = MAZE_NORTH
    elif T_D == 'Left':
        if MO == MAZE_NORTH:
            MO = MAZE_WEST
        elif MO == MAZE_WEST:
            MO = MAZE_SOUTH
        elif MO == MAZE_SOUTH:
            MO = MAZE_EAST
        elif MO == MAZE_EAST:
            MO = MAZE_NORTH  
    elif T_D == 'Back':
        if MO == MAZE_NORTH:
            MO = MAZE_SOUTH
        elif MO == MAZE_SOUTH:
            MO = MAZE_NORTH
        elif MO == MAZE_EAST:
            MO = MAZE_WEST
        elif MO == MAZE_WEST:
            MO = MAZE_EAST  
    else:  
            pass

# what are the right and left direction of the mouse

def RO_LO(MO):
    global RO, LO
    RO = ''
    LO = ''
    if MO == MAZE_NORTH:
        RO = 'e'
        LO = 'w'
    elif MO == MAZE_EAST:
        RO = 's'
        LO = 'n'
    elif MO == MAZE_SOUTH:
        RO = 'w'
        LO = 'e'
    elif MO == MAZE_WEST:
        RO = 'n'
        LO = 's'
    else:
        pass

# Initialize the maze dimensions (grid with 16x16 blocks)
maze_width = 16
maze_height = 16

# Set the initial position of the micromouse
micromouse_x, micromouse_y = 0, 0

# Current position of the micromouse
def update_maze():
    x, y = mazeWidth(), mazeHeight()

# Function to move the mouse forward

def move_forward():
    global micromouse_x, micromouse_y
    moveForward()
    if MO == MAZE_NORTH:
        micromouse_y += 1
    elif MO == MAZE_EAST:
        micromouse_x += 1
    elif MO == MAZE_SOUTH:
        micromouse_y -= 1
    elif MO == MAZE_WEST:
        micromouse_x -= 1

# Function to move the mouse left

def move_left():
    global micromouse_x, micromouse_y, T_D
    turnLeft()
    moveForward()
    T_D = 'Left'
    if MO == MAZE_NORTH:
        micromouse_x -= 1
    elif MO == MAZE_EAST:
        micromouse_y += 1
    elif MO == MAZE_SOUTH:
        micromouse_x += 1
    elif MO == MAZE_WEST:
        micromouse_y -= 1    

# Function to move the mouse right

def move_right():
    global micromouse_x, micromouse_y, T_D
    turnRight()
    moveForward()
    T_D = 'Right'
    if MO == MAZE_NORTH:
        micromouse_x += 1
    elif MO == MAZE_EAST:
        micromouse_y -= 1
    elif MO == MAZE_SOUTH:
        micromouse_x -= 1
    elif MO == MAZE_WEST:
        micromouse_y += 1    

# Function to move the mouse back

def move_back():
    global micromouse_x, micromouse_y, T_D
    turnRight()
    turnRight()
    moveForward()
    T_D = 'Back'
    if MO == MAZE_NORTH:
        micromouse_y -= 1
    elif MO == MAZE_EAST:
        micromouse_x -= 1
    elif MO == MAZE_SOUTH:
        micromouse_y += 1
    elif MO == MAZE_WEST:
        micromouse_x += 1

# Function to navigate the maze using the updated maze matrix
def navigate_maze():
    global MO, RO, LO
    # Initial orientations
    MO = MAZE_NORTH
    RO = 'e'
    LO = 'w'
    BO = 's'
    setWall(micromouse_x, micromouse_y, BO)  
    while not at_center():
        global T_D
        update_maze()
        T_D = ''
        RO_LO(MO)

        #The Micro Mouse Orientation/Direction, which I dont have a direction in my life yet ..... cries here

        if wallFront():
            setWall(micromouse_x, micromouse_y, MO)
        if wallLeft():
            setWall(micromouse_x, micromouse_y, LO)
        if wallRight():
            setWall(micromouse_x, micromouse_y, RO) 

        #The cell is the position of the MM in the Maze

        cell = maze[micromouse_x][micromouse_y]

        #Is there a walll hmmmm this code will tell the cell, kind of a big brain move dont you agree ... maybe not since there is probably a 10x better way that i can't feasibly imagine with this smallish brain ;(

        if MO == MAZE_NORTH:            
            if wallFront():
                cell.n = True
            if wallLeft():
                cell.w = True                
            if wallRight():
                cell.e = True
            # if wallBack():
            #     cell.South = True
        elif MO == MAZE_WEST:
            if wallFront():
                cell.w = True
            if wallLeft():
                cell.s = True
            if wallRight():
                cell.n = True
            # if wallBack():
            #     cell.East = True           
        elif MO == MAZE_EAST:
            if wallFront():
                cell.e = True
            if wallLeft():
                cell.n = True
            if wallRight():
                cell.s = True
            # if wallBack():
            #     cell.West = True
        elif MO == MAZE_SOUTH:
            if wallFront():
                cell.s = True
            if wallLeft():
                cell.e = True
            if wallRight():
                cell.w = True
            # if wallBack(): 
            #     cell.north = True
            
        # print(maze[micromouse_x][micromouse_y+1].value, maze[micromouse_x+1][micromouse_y].value, maze[micromouse_x+1][micromouse_y].value,cell.w,cell.s, cell.n, cell.e, file=sys.stderr)
        cell.value = cell.value + 1

       #How to move or the flood Fill Algorithim By yours Truly Brandon the not so genius Genius MWAHHAHAHHHAHAHHAH, world explodes by this code "pow"

        if micromouse_y+1 <= 15 and micromouse_x+1 <= 15 and micromouse_x-1 >= 0 and micromouse_y-1 >= 0:
            if cell.value > maze[micromouse_x][micromouse_y+1].value and cell.n == False:
                if MO == MAZE_NORTH:
                    move_forward()
                elif MO == MAZE_EAST:
                    move_left()
                elif MO == MAZE_WEST:
                    move_right()
                elif MO == MAZE_SOUTH:
                    move_back()
            elif cell.value > maze[micromouse_x+1][micromouse_y].value and cell.e == False:
                if MO == MAZE_NORTH:
                    move_right()
                elif MO == MAZE_EAST:
                    move_forward()
                elif MO == MAZE_WEST:
                    move_back()
                elif MO == MAZE_SOUTH:
                    move_left()
            elif cell.value > maze[micromouse_x-1][micromouse_y].value and cell.w == False:
                if MO == MAZE_NORTH:
                    move_left()
                elif MO == MAZE_EAST:
                    move_back()
                elif MO == MAZE_WEST:
                    move_forward()
                elif MO == MAZE_SOUTH:
                    move_right()
            elif cell.value > maze[micromouse_x][micromouse_y-1].value and cell.s == False:
                if MO == MAZE_NORTH:
                    move_back()
                elif MO == MAZE_EAST:
                    move_right()
                elif MO == MAZE_WEST:
                    move_left()
                elif MO == MAZE_SOUTH:
                    move_forward()
        elif micromouse_y+1 > 15 and micromouse_x+1 <= 15 and micromouse_x-1 >= 0 and micromouse_y-1 >= 0:
            if cell.value > maze[micromouse_x+1][micromouse_y].value and cell.e == False:
                if MO == MAZE_NORTH:
                    move_right()
                elif MO == MAZE_EAST:
                    move_forward()
                elif MO == MAZE_WEST:
                    move_back()
                elif MO == MAZE_SOUTH:
                    move_left()
            elif cell.value > maze[micromouse_x-1][micromouse_y].value and cell.w == False:
                if MO == MAZE_NORTH:
                    move_left()
                elif MO == MAZE_EAST:
                    move_back()
                elif MO == MAZE_WEST:
                    move_forward()
                elif MO == MAZE_SOUTH:
                    move_right()
            elif cell.value > maze[micromouse_x][micromouse_y-1].value and cell.s == False:
                if MO == MAZE_NORTH:
                    move_back()
                elif MO == MAZE_EAST:
                    move_right()
                elif MO == MAZE_WEST:
                    move_left()
                elif MO == MAZE_SOUTH:
                    move_forward()
        elif micromouse_y+1 <= 15 and micromouse_x+1 > 15 and micromouse_x-1 >= 0 and micromouse_y-1 >= 0:
            print('works', file=sys.stderr)
            if cell.value > maze[micromouse_x][micromouse_y+1].value and cell.n == False:
                if MO == MAZE_NORTH:
                    move_forward()
                elif MO == MAZE_EAST:
                    move_left()
                elif MO == MAZE_WEST:
                    move_right()
                elif MO == MAZE_SOUTH:
                    move_back()
            elif cell.value > maze[micromouse_x-1][micromouse_y].value and cell.w == False:
                if MO == MAZE_NORTH:
                    move_left()
                elif MO == MAZE_EAST:
                    move_back()
                elif MO == MAZE_WEST:
                    move_forward()
                elif MO == MAZE_SOUTH:
                    move_right()
            elif cell.value > maze[micromouse_x][micromouse_y-1].value and cell.s == False:
                if MO == MAZE_NORTH:
                    move_back()
                elif MO == MAZE_EAST:
                    move_right()
                elif MO == MAZE_WEST:
                    move_left()
                elif MO == MAZE_SOUTH:
                    move_forward()
        elif micromouse_y+1 <= 15 and micromouse_x+1 <= 15 and micromouse_x-1 < 0 and micromouse_y-1 >=0:
            if cell.value > maze[micromouse_x][micromouse_y+1].value and cell.n == False:
                if MO == MAZE_NORTH:
                    move_forward()
                elif MO == MAZE_EAST:
                    move_left()
                elif MO == MAZE_WEST:
                    move_right()
                elif MO == MAZE_SOUTH:
                    move_back()
            elif cell.value > maze[micromouse_x+1][micromouse_y].value and cell.e == False:
                if MO == MAZE_NORTH:
                    move_right()
                elif MO == MAZE_EAST:
                    move_forward()
                elif MO == MAZE_WEST:
                    move_back()
                elif MO == MAZE_SOUTH:
                    move_left()
            elif cell.value > maze[micromouse_x][micromouse_y-1].value and cell.s == False:
                if MO == MAZE_NORTH:
                    move_back()
                elif MO == MAZE_EAST:
                    move_right()
                elif MO == MAZE_WEST:
                    move_left()
                elif MO == MAZE_SOUTH:
                    move_forward()
        elif micromouse_y+1 > 15 and micromouse_x+1 <= 15 and micromouse_x-1 < 0 and micromouse_y-1 >= 0:
            if cell.value > maze[micromouse_x+1][micromouse_y].value and cell.e == False:
                if MO == MAZE_NORTH:
                    move_right()
                elif MO == MAZE_EAST:
                    move_forward()
                elif MO == MAZE_WEST:
                    move_back()
                elif MO == MAZE_SOUTH:
                    move_left()
            elif cell.value > maze[micromouse_x][micromouse_y-1].value and cell.s == False:
                if MO == MAZE_NORTH:
                    move_back()
                elif MO == MAZE_EAST:
                    move_right()
                elif MO == MAZE_WEST:
                    move_left()
                elif MO == MAZE_SOUTH:
                    move_forward()
        elif micromouse_y+1 > 15 and micromouse_x+1 > 15 and micromouse_x-1 >= 0 and micromouse_y-1 >= 0:
            if cell.value > maze[micromouse_x-1][micromouse_y].value and cell.w == False:
                if MO == MAZE_NORTH:
                    move_left()
                elif MO == MAZE_EAST:
                    move_back()
                elif MO == MAZE_WEST:
                    move_forward()
                elif MO == MAZE_SOUTH:
                    move_right()
            elif cell.value > maze[micromouse_x][micromouse_y-1].value and cell.s == False:
                if MO == MAZE_NORTH:
                    move_back()
                elif MO == MAZE_EAST:
                    move_right()
                elif MO == MAZE_WEST:
                    move_left()
                elif MO == MAZE_SOUTH:
                    move_forward()
        elif micromouse_y+1 <= 15 and micromouse_x+1 <= 15 and micromouse_x-1 < 0 and micromouse_y-1 < 0:
            if cell.value > maze[micromouse_x][micromouse_y+1].value and cell.n == False:
                if MO == MAZE_NORTH:
                    move_forward()
                elif MO == MAZE_EAST:
                    move_left()
                elif MO == MAZE_WEST:
                    move_right()
                elif MO == MAZE_SOUTH:
                    move_back()
            elif cell.value > maze[micromouse_x+1][micromouse_y].value and cell.e == False:
                if MO == MAZE_NORTH:
                    move_right()
                elif MO == MAZE_EAST:
                    move_forward()
                elif MO == MAZE_WEST:
                    move_back()
                elif MO == MAZE_SOUTH:
                    move_left()
        else:
            print("NONONONONOONONONONONONONONONONONONO WHY ME", file=sys.stderr)
 
          
        update_MO(T_D)
        print(micromouse_x,micromouse_y+1, cell.value, MO, RO, LO, file=sys.stderr)

# Function to check if the mouse is at the center of the maze
def at_center():
    return micromouse_x == maze_width // 2 and micromouse_y == maze_height // 2

# Main function to solve the maze
def solve_maze():
    navigate_maze()

# Call the function to solve the maze
solve_maze()  