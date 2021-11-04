############################ imports ###################################
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from copy import deepcopy
from matplotlib.animation import FuncAnimation

########################### constants ##################################
# grid size
sizex = 500
sizey = 50

# # colors
# cmap = colors.ListedColormap(['black', 'white', 'red', 'blue', 'green', 'yellow', 'cyan', 'magenta'])

#animation
frames = 500
fps = 10

############################# classes ##################################

class block:

    '''
    Individual blocs of GoT
    '''

    def __init__(self, i, j, state):
        self.i = i
        self.j = j
        self.state = state
        self.color = state
        self.desaturate = False

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
                    if (0 <= (self.i + x) < sizey) and (0 <= (self.j + y) < sizex):
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
    
    def elementar(self, last_line):
        
        state = 0

        if (last_line[self.j].state == 0) and (last_line[self.j].state == last_line[self.j+1].state):
            state = last_line[self.j-1].state
        else:
            state = int(not bool(last_line[self.j-1].state))
        
        return state


class table:

    '''
    Table for organizing matriz that is used for controlling blocks
    '''

    def __init__(self, matrix, Nx, Ny):
        self.grid = [[block(i, j, matrix[i][j]) for j in range(0, Nx)] for i in range(0, Ny)]
        self.last_line = self.grid[-1]
        self.sizey = Ny
        self.sizex = Nx

    def floats_matrix(self):
        return [[int(self.grid[i][j].color) for j in range(0, self.sizex)] for i in range(0, self.sizey)]

    def update_gol(self):
        '''
        update grid do decide next frame
        '''
        pivo_grid = deepcopy(self.grid)
        for col in range(0, int(self.sizey*9/10)):
            for lin in range(0, self.sizex):
                pivo = pivo_grid[col][lin].tanatos(pivo_grid)
                self.grid[col][lin].state = pivo
                if pivo == 1:
                    self.grid[col][lin].color += 1
                    self.grid[col][lin].desaturate = False
                else:
                    if self.grid[col][lin].color > 0:
                        self.grid[col][lin].color /= 1.1


    def update_ca(self):
        '''
        update grid do decide next frame
        '''

        pivo_line = deepcopy(self.last_line)

        for lin in range(int(self.sizey*9/10)-1, self.sizey-1):
            self.grid[lin] = deepcopy(self.grid[lin+1])
            
        for col in range(1, self.sizex-1):
            pivo = pivo_line[col].elementar(pivo_line)
            self.grid[self.sizey-1][col].state = pivo
            self.grid[self.sizey-1][col].color = pivo * 10


        self.last_line = deepcopy(self.grid[self.sizey-1])

####################### auxiliar functions #############################

def read_init_state(file, N):
    with open(file, 'r') as file:
        matrix = [[int(num) for num in file.readline()[:-1].split(' ')] for i in range(0, N)]
    return matrix


def malha(sizex, sizey):
    aux = [[0 for i in range(0, sizex)] for j in range(0, int(sizey))]
    aux[-1][int(len(aux[0])/2)] = 1
    return aux

############################## main program ############################

if __name__ == '__main__':

    init = malha(sizex, sizey)
    got = table(init, sizex, sizey)
    fig, ax = plt.subplots()

    def animate(i):
        got.update_ca()
        ax.imshow(got.floats_matrix(), cmap="inferno", vmin=0, vmax=6)
        got.update_gol()

    anim = FuncAnimation(fig, animate, frames=frames)
    anim.save('mix5.gif', fps=fps)
