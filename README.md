# PathFinder
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
