############################ imports ###################################
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from copy import deepcopy
from matplotlib.animation import FuncAnimation

########################### constants ##################################
# grid size
size = 50
# colors
cmap = colors.ListedColormap(['black', 'white'])

############################# classes ##################################

class block:

    '''
    Individual blocs of GoT
    '''

    def __init__(self, i, j, state):
        self.i = i
        self.j = j
        self.state = state

    def tanatos(self, grid):
        
        '''
        Greek personification of Death, control if a block lives. 
        '''
        state = 0
        count = 0

        # how many blocks are alive?
        for x in range(-1,2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    pass
                else:
                    if (0 <= (self.i + x) < size) and (0 <= (self.j + y) < size):
                        count += grid[self.i + x][self.j + y].state
                        
        # game conditions
        if count < 2: 
            state = 0
        elif count == 2:
            if self.state == 1:
                state = 1
            else:
                state = 0
        elif count == 3:
            state = 1
        elif count > 3:
            if self.state == 1:
                state = 0
        
        return state

class table:

    '''
    Table for organizing matriz that is used for controlling blocks
    '''

    def __init__(self, matrix, N):
        self.grid = [[block(i, j, matrix[i][j]) for j in range(0, N)] for i in range(0, N)]
        self.size = N

    def floats_matrix(self):
        return [[float(self.grid[i][j].state) for j in range(0, self.size)] for i in range(0, self.size)]

    def update(self):
        '''
        update grid do decide next frame
        '''
        pivo_grid = deepcopy(self.grid)
        for col in range(0, self.size):
            for lin in range(0, self.size):
                self.grid[col][lin].state = pivo_grid[col][lin].tanatos(pivo_grid)

####################### auxiliar functions #############################

def read_init_state(file, N):
    with open(file, 'r') as file:
        matrix = [[int(num) for num in file.readline()[:-1].split(' ')] for i in range(0, N)]
    return matrix

############################## main program ############################

if __name__ == '__main__':

    init = read_init_state("cannon.txt", size)
    got = table(init, size)
    fig, ax = plt.subplots()

    # ax.imshow(got.floats_matrix(), cmap=cmap)
    # plt.show()

    def animate(i):
        ax.imshow(got.floats_matrix(), cmap=cmap)
        got.update()

    anim = FuncAnimation(fig, animate, frames=200)
    anim.save('cannon.gif', fps=20)



