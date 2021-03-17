from tkinter import *
import random
import time


def display_maze(maze, path, shortest_path, title):
    root = Tk()
    root.title('Maze Simulation')
    root.geometry("950x950")
    # Creating canvas
    canvas = Canvas(root, width=2000, height=2000, bg='white')
    canvas.place(x=0, y=0)

    # drawing the maze
    x1 = 100
    y1 = 100
    for x in range(len(maze)):
        for y in range(len(maze[0])):

            if maze[x][y] == 0:
                canvas.create_rectangle(x1, y1, x1 + 20, y1 + 20, fill='black')
            elif maze[x][y] == 2 or (x == 0 and y == 0):
                canvas.create_rectangle(x1, y1, x1 + 20, y1 + 20, fill='red')
            else:
                if (x, y) in path:
                    canvas.create_rectangle(x1, y1, x1 + 20, y1 + 20, fill='white')
                else:
                    canvas.create_rectangle(x1, y1, x1 + 20, y1 + 20, fill='white')

            x1 += 20
        x1 = 100
        y1 += 20
    end_x = 115 + len(maze[0]) * 20
    end_y = 95 + len(maze) * 20
    rat = canvas.create_oval(105, 105, 115, 115, fill='black')
    canvas.create_text(300, 50, text=title, font=('Helvetica', 20))

    # moving the rat and updating the tile colours
    count = 0

    def start():
        nonlocal count
        if count == 0:
            i = 0
            while True:

                current_x = path[i][1]
                next_x = path[i + 1][1]
                current_y = path[i][0]
                next_y = path[i + 1][0]

                if next_x - current_x == 1:
                    xspeed, yspeed = 20, 0
                if next_x - current_x == -1:
                    xspeed, yspeed = -20, 0
                if next_y - current_y == 1:
                    xspeed, yspeed = 0, 20
                if next_y - current_y == -1:
                    xspeed, yspeed = 0, -20

                x1 = 100 + current_x * 20
                y1 = 100 + current_y * 20
                if (current_x, current_y) != path[0]:
                    canvas.create_rectangle(x1, y1, x1 + 20, y1 + 20, fill='grey')
                # to make sure rat isn't covered by the grey tile
                canvas.tag_raise(rat)

                canvas.move(rat, xspeed, yspeed)
                # adjusting the speed of the simualation
                if len(maze) < 10:
                    time_interval = 0.4
                elif len(maze) < 20:
                    time_interval = 0.15
                else:
                    time_interval = 0.08
                if count1 == 0:
                    time.sleep(time_interval)
                root.update()

                i += 1
                # if the rat has reached the end point
                if i == len(path) - 1:
                    time.sleep(0.5)
                    # displays the time taken
                    text_y = 150 + 20 * len(maze)
                    canvas.create_text(300, text_y, text='Time Taken     : ' + str(len(path) - 1),
                                       font=('Helvetica', 15))
                    canvas.create_text(300, text_y + 30, text='Minimum Time : ' + str(len(shortest_path)), \
                                       font=('Helvetica', 15))
                    # displays the shortest path found using recursion
                    for tile in shortest_path:
                        x1 = 100 + 20 * tile[1]
                        y1 = 100 + 20 * tile[0]
                        canvas.create_rectangle(x1, y1, x1 + 20, y1 + 20, fill='red')
                    break
                # Updating counter
                count += 1

    count1 = 0

    def end():
        nonlocal count1
        # Updating counter
        count1 += 1

    # Creating start and stop buttons
    start_button = Button(root, text="Start", command=start)
    start_button.place(x=50, y=100)
    end_button = Button(root, text="End", command=end)
    end_button.place(x=end_x, y=end_y)
    root.mainloop()


def Maze(n=2):
    '''
    Returns a nested list representing a 2D matrix(maze)
    -------
    maze : List
            0 - wall - position which cannot be occupied,
            1 - tile - position which can be occupied,
            2 - end point - simulation ends when this point is occupied

    '''
    maze1 = [[1, 0, 1, 1, 1, 0, 0, 1, 0],
             [1, 0, 1, 0, 1, 0, 1, 1, 1],
             [1, 1, 1, 0, 1, 0, 1, 0, 1],
             [0, 1, 0, 0, 1, 0, 1, 0, 1],
             [0, 1, 1, 1, 1, 1, 1, 0, 2]]

    maze2 = [[1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
             [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
             [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
             [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
             [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
             [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 2]]

    maze3 = [[1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
             [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
             [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
             [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
             [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
             [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
             [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2]]

    if n == 1:
        return maze1
    if n == 2:
        return maze2
    if n == 3:
        return maze3


def nextTiles(x, y, h, w):
    '''
    Parameters
    ----------
    x : int
        current row
    y : int
        current column
    h : int
        height of maze
    w : int
        width of maze

    Returns
    -------
    nextLocs : list
    contains the postions of surrounding tiles
    with respect to the current position

    '''
    nextLocs = []
    for loc in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        # making sure next positions are valid
        if 0 <= loc[0] < h and 0 <= loc[1] < w and Maze(choice)[loc[0]][loc[1]] != 0:
            nextLocs.append(loc)
    return nextLocs


path = []


def simulation(maze, x=0, y=0):
    '''
    Parameters
    ----------
    maze : list
    x : int
        Starting row
    y : int
        Starting column

    Returns
    -------
    timeSteps : int
        Number of steps taken to complete the maze

    '''
    pos = maze[x][y]
    path.append((x, y))
    # stores previously occupied tiles
    memory = []
    timeSteps = 0
    memory.append((x, y))
    width = len(maze[0])
    height = len(maze)

    while pos != 2:

        preferred_tiles = []
        nextPositions = nextTiles(x, y, height, width)

        # stores the number of times each tile has been visited
        loc_frequency = []
        for loc in nextPositions:
            loc_frequency.append(memory.count(loc))

        # gives preference to the least visited tile(s)
        for i in range(len(nextPositions)):
            min_frequency = min(loc_frequency)
            if loc_frequency[i] == min_frequency:
                preferred_tiles.append(nextPositions[i])

        nextTile = random.choice(preferred_tiles)

        # updating the position variables
        x = nextTile[0]
        y = nextTile[1]
        pos = maze[x][y]

        memory.append(nextTile)
        timeSteps += 1

        if maze[x][y] == 2:
            # indicates the end point
            path.append((x, y))
        else:
            # indicates an explored tile
            path.append((x, y))

    return timeSteps


mem = []
shortest_path = []


# using recursion to find shortest possible time
def recursion(maze, x=0, y=0):
    '''
    Parameters
    ----------
    maze : list
    x : int
    y : int

    Returns
    -------
    bool
        Return True only when the endpoint is reached, false if the position
        is invalid and undergoes recursion in all other cases

    '''
    # checking if the position is within the maze boundaries
    if (0 <= x < len(maze) and 0 <= y < len(maze[0])) == False:
        return False

    pos = maze[x][y]
    # checking if tile has already been occupied to prevent an infinite loop
    if (x, y) not in mem:
        mem.append((x, y))
    else:
        return False

    # checking if the position is a wall
    if pos == 0:
        return False
    # checking if the position is the endpoint
    elif pos == 2:
        return True
    # using recursion to explore all valid paths
    else:
        if recursion(maze, x + 1, y) == True:
            shortest_path.append((x + 1, y))
            return True
        if recursion(maze, x - 1, y) == True:
            shortest_path.append((x - 1, y))
            return True
        if recursion(maze, x, y + 1) == True:
            shortest_path.append((x, y + 1))
            return True
        if recursion(maze, x, y - 1) == True:
            shortest_path.append((x, y - 1))
            return True


# executing the program
try:
    choice = int(input('Select mode:\n1 - Easy \n2 - Medium \n3 - Hard\n'))
    num_trials = int(input('Enter the number of trials: '))

    # running the simulation
    total_time = 0
    for i in range(num_trials):
        path = []
        total_time += simulation(Maze(choice))
    print('Average time taken:', total_time / num_trials)

    # running the recursion function
    recursion(Maze(choice))
    print('Shortest possible time:', len(shortest_path))
    # displaying the solution
    display_maze(Maze(choice), path, shortest_path, 'Maze Simulation')

except Exception:
    print('Invalid choice.')