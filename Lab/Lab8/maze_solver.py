"""
COMP 1023 Lab 8: Maze Pathfinding
Student Implementation File

Instructions:
- Implement the three TODO functions below
- DO NOT modify function signatures
- You may add helper functions if needed
- Test your code using maze_tester.py (GUI)
"""

import copy

# Direction for reference
DIRECTIONS = ['R', 'L', 'U', 'D']
DELTA = [[1, 0], [-1, 0], [0, -1], [0, 1]]

def parse_maze(maze):
    '''
    Task 1: Parse the maze to extract start, end, and teleporter pairs.
    
    Parameters:
        maze: 2D list of single characters
    
    Returns:
        tuple: (start, end, teleport_info)
            - start: list [x, y] coordinate of 'S'
            - end: list [x, y] coordinate of 'E'  
            - teleport_info: list of information list of paired teleporters, within the format:
                [ ['A', [x1, y1], [x2, y2]], ['B', [x3, y3], [x4, y4]], ...]

    Example:
        maze = [
            ['#', '#', '#', '#'],
            ['#', 'S', 'A', '#'],
            ['#', '1', '2', '#'],
            ['#', 'A', 'E', '#'],
            ['#', '#', '#', '#']
        ]
        Returns: ([1, 1], [2, 3], [['A', [2, 1], [1, 3]]])
    '''
    # TODO: Implement this function
    teleport_info = []
    teleport_index : dict[str, int] = {}

    for i in range(len(maze)):
        if 'S' in maze[i]:
            index_s = [maze[i].index('S'), i]
        if 'E' in maze[i]:
            index_e = [maze[i].index('E'), i]
        for j in range(len(maze[i])):
            x = maze[i][j]
            if x >= 'A' and x <= 'Z' and x != 'S' and x != 'E':
                if x in teleport_index:
                    teleport_info[teleport_index[x]].append([j,i])
                else:
                    teleport_info.append([x, [j, i]])
                    teleport_index[x] = len(teleport_info)-1
    teleport_info.sort(key = lambda x: ord(x[0]))
    for i in teleport_info:
        if len(i) > 3:
            teleport_info.remove(i)
    return index_s, index_e, teleport_info

def dfs_helper_shortest(maze, end, teleport_info, height, width,
                        current_pos, current_path, visited):
    """
    Task 2: DFS helper recursive function for finding the Shortest Path.

    Parameters:
        maze: 2D list of characters
        end: list [x, y] target position
        teleport_info: [['A', [x1, y1], [x2, y2]], ...]
        height, width: maze dimensions
        current_pos: list [x, y]
        current_path: list of direction chars
        visited: list of positions [x, y] that have been visited

    Return:
        - best_path: list of direction chars for the best path (with lowest steps)
                     that could lead to the end position found in this branch,
                     or empty list if path has not been found
        - example: ['R', 'D', 'L', ...]      
    """

    # Base case: in this branch, we have reached the end position
    # this path is apparently the best path found in this branch
    
    if current_pos == end:
        return current_path[:]
        
    best_path = []

    for direction in DIRECTIONS:
        delta = DELTA[DIRECTIONS.index(direction)]

        # TODO: Calculate next_pos using delta
        # ------- Modify the line below -------
        next_pos: list = [current_pos[0]+delta[0], current_pos[1]+delta[1]]
        # ------- Modify the line above -------

        # TODO: Validate if next_pos is within bounds, not a wall, and not visited
        # ------- Modify the line below -------
        if maze[next_pos[1]][next_pos[0]] == '#' \
        or next_pos[0] < 0 or next_pos[0] >= width \
        or next_pos[1] < 0 or next_pos[1] >= height \
        or next_pos in visited:
            continue
        # ------- Modify the line above -------

        # TODO: Handle teleporter if next_pos is a teleporter, update next_pos accordingly
        #       and validate if the teleported position is visited again if teleported
        # ------- Modify the line below -------
        tmp = False
        for i in teleport_info:
            if i[1] == next_pos and (i[2] not in visited):
                next_pos = i[2]
                visited.append(i[1])
                tmp = True
                x = i[1]
                y = i[2]
                break
            if i[2] == next_pos and (i[1] not in visited):
                next_pos = i[1]
                tmp = True
                visited.append(i[2])
                x = i[1]
                y = i[2]
                break

        # ------- Modify the line above ---------

        # TODO: Update visited and current_path, prepare for recursive call
        # ------- Modify the line below -------
        visited.append(next_pos)
        current_path.append(direction)
        # ------- Modify the line above -------

        path = dfs_helper_shortest(maze, end, teleport_info, height, width, 
                                   next_pos, current_path, visited)
        
        if path:
            if (not best_path) or (len(path) < len(best_path)):
                best_path = copy.deepcopy(path)

        # TODO: Backtrack - undo changes to visited and current_path
        # ------- Modify the line below -------
        if tmp:
            visited.remove(x)
            visited.remove(y)
        else:
            visited.remove(next_pos)
        current_path.pop()
        # ------- Modify the line above -------

    return best_path

def dfs_helper_max_score(maze, end, teleport_info, height, width,
                         current_pos, current_path, current_score, visited):
    """
    Task 3: DFS helper recursive function for finding the Maximum Score.

    Parameters:
        maze: 2D list of characters
        end: list [x, y] target position
        teleport_info: [['A', [x1, y1], [x2, y2]], ...]
        height, width: maze dimensions
        current_pos: list [x, y]
        current_path: list of direction chars
        current_score: integer, total score accumulated so far
        visited: list of positions [x, y] that have been visited
    
    Return:
        tuple (best_path, max_score):
        - best_path: list of direction chars for the best path (with maximum score)
                     that could lead to the end position found in this branch,
                     or empty list if path has not been found
            - example: ['R', 'D', 'L', ...]
        - max_score: integer, total score of the best_path found,
                     or 0 if no path has been found

    Since the structure is similar to Task 2, we will not provide detailed comments here.
    """

    # TODO: Handle the base case of this function
    # ------- Modify the line below -------
    if current_pos == end:
        return current_path, current_score
    # ------- Modify the line above -------

    best_path = []
    max_score = 0
        
    for direction in DIRECTIONS:
        # TODO: Calculate and validate next_pos
        # ------- Modify the line below -------
        delta = DELTA[DIRECTIONS.index(direction)]
        next_pos: list = [current_pos[0]+delta[0], current_pos[1]+delta[1]]
        # ------- Modify the line above -------

        # TODO: Update parameters, do recursive call
        # ------- Modify the line below -------
        if maze[next_pos[1]][next_pos[0]] == '#' \
        or next_pos[0] < 0 or next_pos[0] >= width \
        or next_pos[1] < 0 or next_pos[1] >= height \
        or next_pos in visited:
            continue
        
        tmp = False
        for i in teleport_info:
            if i[1] == next_pos and (i[2] not in visited):
                next_pos = i[2]
                visited.append(i[1])
                tmp = True
                x = i[1]
                y = i[2]
                break
            if i[2] == next_pos and (i[1] not in visited):
                next_pos = i[1]
                tmp = True
                visited.append(i[2])
                x = i[1]
                y = i[2]
                break

        visited.append(next_pos)
        current_path.append(direction)
        val = maze[next_pos[1]][next_pos[0]]
        if val >= '0' and val <= '9':
            current_score += int(val)

        path = dfs_helper_max_score(maze, end, teleport_info, height, width, 
                                   next_pos, current_path, current_score, visited)
        
        
        # ------- Modify the line above -------

        # TODO: Update the best path and maximum score, and do the backtracking
        # ------- Modify the line below -------
        if path[0]:
            if path[1] > max_score:
                best_path = copy.deepcopy(path[0])
                max_score = path[1]
        current_path.pop()
        if val >= '0' and val <= '9':
            current_score -= int(val)
        if tmp:
            visited.remove(x)
            visited.remove(y)
        else:
            visited.remove(next_pos)
        # ------- Modify the line above -------

    return best_path, max_score

def find_shortest_path_dfs(maze, start, end, teleport_info):
    '''
    Utilize your implemented function to find the shortest path from start to end.
    Already implemented, no need to modify.
    '''
    
    height = len(maze)
    width = len(maze[0])
    
    initial_visited = [start]
    best_solution = dfs_helper_shortest(maze, end, teleport_info, height, width,
                                        start, [], initial_visited)

    if best_solution:
        return (True, best_solution, len(best_solution))
    else:
        return (False, [], None)

def find_max_score_path(maze, start, end, teleport_info):
    '''
    Utilize your implemented function to find the maximum score path from start to end.
    Already implemented, no need to modify.
    '''

    height = len(maze)
    width = len(maze[0])
    
    initial_visited = [start]
    best_solution, max_score = dfs_helper_max_score(maze, end, teleport_info, height, width,
                                                    start, [], 0, initial_visited)
    
    found = bool(best_solution)
    return (found, best_solution, max_score)