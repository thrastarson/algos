#Robot in a grid. Imagine a robot sitting in the upper left corner of a grid
#with r rows and c columns. The robot can only move in two directions,
#right and down, but certain cells are "off limits" such that the robot
#cannot step on them. Design an algorithm to find a path for the robot
#from the top left to the bottom right.
def has_path(n, m, clear):

    if n < 0 or n >= len(clear) or m < 0 or m >= len(clear[0]):
        return False

    if n == 0 and m == 0 and clear[n][m]:
        return True
    
    return clear[n, m] and (has_path(n, m-1, clear) or has_path(n-1, m, clear))