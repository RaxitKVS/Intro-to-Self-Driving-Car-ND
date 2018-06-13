import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    height = len(grid)
    width = len(grid[0])
    for i in range(height):
        row = []
        for j in range(width):
            #pdb.set_trace()
            if color == grid[i][j]:
                prob = beliefs[i][j] * p_hit
            elif color != grid[i][j]:
                prob = beliefs[i][j] * p_miss
            row.append(prob)
        new_beliefs.append(row)
    a = 0
    for i in range(len(new_beliefs)):
        for j in range(len(new_beliefs[0])):
            a = a + new_beliefs[i][j]
    
    for i in range(len(new_beliefs)):
        for j in range(len(new_beliefs)):
            new_beliefs[i][j] = new_beliefs[i][j] /a
    #
    # TODO - implement this in part 2
    #
    
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy) % height
            new_j = (j + dx) % width
            # pdb.set_trace()
            new_G[int(new_j)][int(new_i)] = cell
    return blur(new_G, blurring)