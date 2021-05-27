import numpy
import pygame

# Creates empty dictionary where value = matrix index/number of neighbors
def create_cells(grid_size):
    cell_record = {}
    for i in range(1, grid_size+1):
        cell_record[i] = 0
    return cell_record

# Updates numbers of neighbors for each matrix index in records dictionary
def update_cells(record, updated_cells):
    for key in updated_cells.keys():
        record[key] = updated_cells[key]

# Creates dictionary where value = matrix index/cell state (alive or dead)
def get_cell_states(grid):
    cell_count = 0
    cell_states = {}
    for x in range(len(grid)):
        for y in range(len(grid)):
            cell_count += 1
            cell_states[cell_count] = int(grid[x][y])
    return cell_states

# Check through cells, implementing Conway's Game of Life rules
def update_state(states, record):
    for key in states.keys():
        if (states[key] == 0) and (record[key] == 3):
            states[key] = 1
        elif (states[key] == 1):
            states[key] = 0
            if record[key] == 2 or record[key] == 3:
                states[key] = 1 

# Finds the number of neighbors per cell in matrix
def check_neighbors(grid, x, y):
    counter = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i >= 0) and (j >= 0) and (i < (len(grid))) and (j < (len(grid))):
                if i != x or j != y:
                    if grid[i][j] == 1:
                        counter += 1
    return counter

# Traverses through matrix
def search_grid(grid):
    cells = {}
    cell_count = 0
    for x in range(len(grid)):
        for y in range(len(grid)):
            cell_count += 1
            cells[cell_count] = check_neighbors(grid, x, y)
    return cells

# Updates states on each index in matrix
def update_grid(grid, states):
    counter = 0
    for x in range(len(grid)):
        for y in range(len(grid)):
            counter += 1
            grid[x][y] = states[counter] 

# Prints visual representation of matrix
def print_grid(grid):
    for x in range((len(grid))):
        for y in range((len(grid))):
            if grid[x][y] == 0:
                print('·', end='')
            elif grid[x][y] == 1:
                print('●', end='')
        print("")

GRID_SIZE = 45
RUNS = 1000

pygame.init()
screen = pygame.display.set_mode((GRID_SIZE,GRID_SIZE), pygame.RESIZABLE)

grid = numpy.zeros((GRID_SIZE,GRID_SIZE))
cell_record = create_cells(GRID_SIZE*GRID_SIZE)

# gosper's glider gun
# block
grid[19][1] = 1
grid[19][2] = 1
grid[20][1] = 1
grid[20][2] = 1

# block
grid[17][35] = 1
grid[17][36] = 1
grid[18][35] = 1
grid[18][36] = 1

# structure
grid[17][13] = 1
grid[17][14] = 1
grid[18][12] = 1
grid[19][11] = 1
grid[20][11] = 1
grid[21][11] = 1
grid[22][12] = 1
grid[23][13] = 1
grid[23][14] = 1
grid[20][15] = 1
grid[18][16] = 1 
grid[22][16] = 1
grid[19][17] = 1
grid[20][17] = 1 
grid[20][18] = 1
grid[21][17] = 1

# structure
grid[17][21] = 1
grid[18][21] = 1
grid[19][21] = 1
grid[17][22] = 1
grid[18][22] = 1
grid[19][22] = 1
grid[16][23] = 1
grid[20][23] = 1
grid[16][25] = 1
grid[15][25] = 1
grid[20][25] = 1
grid[21][25] = 1


for i in range(RUNS):
    update_cells(cell_record, search_grid(grid))
    states = get_cell_states(grid)
    update_state(states, cell_record)
    update_grid(grid, states)
    surf = pygame.surfarray.make_surface(grid)
    screen.blit(surf, (0,0))
    pygame.display.update()