import 
from curses import wrapper
import queue
import time 

maze = [
    ["#","#","#","#","#","O","#","#","#"],
    ["#"," "," "," "," "," "," "," ","#"],
    ["#"," ","#","#"," ","#","#"," ","#"],
    ["#"," ","#"," "," "," ","#"," ","#"],
    ["#"," ","#"," ","#"," ","#"," ","#"],
    ["#"," ","#"," ","#"," ","#"," ","#"],
    ["#"," ","#"," ","#"," ","#","#","#"],
    ["#"," "," "," "," "," "," "," ","#"],
    ["#","#","#","#","#","#","#","X","#"]
]

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1) #Default maze as blue
    RED = curses.color_pair(2) #Path in the maze as red
    for i, row in enumerate(maze): #enumerate gives the index and value of a variable. i is the index of the row you are currently, row is the entire row itself
        for j, value in enumerate(row): #j is the index of the variables in the row (columns), value is the value of each individual variable
            if (i,j) in path:
                stdscr.addstr(i, j*2, "X", RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE) # i, j is the position and value is the variable

def find_start(maze, start): #Function to find the starting position
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i,j
            
    return None

def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)
    #Setting up the queue
    q = queue.Queue() #module.function/class()
    q.put((start_pos, [start_pos])) #Inserts a tuple containing the starting position & a list of the starting position (want to keep track of the node you want to 
    #process next as well as the path (the list) to get to that node)
    visited = set()
    
    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos
        
        stdscr.clear() 
        print_maze(maze, stdscr, path)
        time.sleep(0.2) #To slow down the algorithm
        stdscr.refresh() 
        
        if maze[row][col] == end:
            return path
        
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            
            r, c = neighbor
            if maze[r][c] == "#":
                continue
            
            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)

def find_neighbors(maze, row, col):
    neighbors = []
    
    if row > 0: #UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze): #DOWN
        neighbors.append((row + 1, col))
    if col > 0: #LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze): #RIGHT
        neighbors.append((row, col + 1))
    
    return neighbors


#Using the curses module
def main(stdscr): #Standard output screen: used to create output, don't need print statements
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) #ID of color pair, Foreground color, background color (of the text)
    
    #stdscr.clear() #To clear the screen
    #print_maze(maze, stdscr)
    #stdscr.addstr(5,5, "hello world!", blue_and_black) #Enter the position and whatever text you want to display on the screen. 1st value for rows and 2nd for columns
    #stdscr.refresh() #So see what we wrote
    find_path(maze, stdscr)
    stdscr.getch() #Waits for user to to do something before exiting the program
    
wrapper(main) #Initializes the curses module, calls the function and passes the stdscr which can be used to control the output

"""
How does the breath first search algorithm solving the maze work?

- The goal is to continuously expand outwards from a point until you find the point you are looking for (the ending node).
- Each of the squares are referred to as nodes according to graph theory
- We start at the starting point and slowly expand outwards by looking at the neighbors of that point
- Then you look at the neighbors of the neighbors (avoid path blockers), done one neighbor at a time
- Continue until you find the ending node. 

- Queues are used to implement this algorithm (FIFO)
- Put the current position node to the front, take the position node at the top out and process it by finding its neighbors then put the neighbors into the queue
- Check if the neighbors are the ending node during each step
- Add the visited elements into the visited tuple
- As soon as the ending node is drawn, we can trace the path
"""

