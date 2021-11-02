############################ imports ###################################
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from copy import deepcopy
from matplotlib.animation import FuncAnimation

########################### constants ##################################
# grid size
size = 100

#animation config
frames = 50
fps = 10

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

    def elementar(self, last_line):
        
        state = 0

        if (last_line[self.j].state == 0) and (last_line[self.j].state == last_line[self.j+1].state):
            state = last_line[self.j-1].state
        else:
            state = int(not bool(last_line[self.j-1].state))

        return state

    def totalistic(self, last_line):

        state = 0

        if  last_line[self.j-1].state == last_line[self.j+1].state:
            state = 0
        else:
            state = 1

        return state

    def outer_totalistic(self, last_line):

        state = 0

        if  last_line[self.j-1].state == last_line[self.j+1].state:
            if self.state == 0:
                state = 0
            else:
                state = 1
        else:
            if self.state == 0:
                state = 1
            else:
                state = 0

        return state


class table:

    '''
    Table for organizing matriz that is used for controlling blocks
    '''

    def __init__(self, init_line, N):
        self.grid = [[block(i, j, 0) for j in range(0, N)] for i in range(0, N)]
        self.grid[-1] = [block(size, j, init_line[j]) for j in range(0, N)]
        self.last_line = self.grid[-1]
        self.size = N

    def floats_matrix(self):
        return [[float(self.grid[i][j].state) for j in range(0, self.size)] for i in range(0, self.size)]

    def update(self):
        '''
        update grid do decide next frame
        '''

        pivo_line = deepcopy(self.last_line)

        for lin in range(1, self.size-1):
            self.grid[lin] = deepcopy(self.grid[lin+1])
            
        for col in range(1, self.size-1):
            self.grid[size-1][col].state = pivo_line[col].totalistic(pivo_line)

        self.last_line = deepcopy(self.grid[size-1])

####################### auxiliar functions #############################

def read_init_state(file, N):
    with open(file, 'r') as file:
        line = [int(num) for num in file.readline()[:-1].split(' ')]
    return line

############################## main program ############################

if __name__ == '__main__':

    init = read_init_state("txts/ln_100.txt", size)
    got = table(init, size)
    fig, ax = plt.subplots()

    def animate(i):
        ax.imshow(got.floats_matrix(), cmap=cmap)
        got.update()

    anim = FuncAnimation(fig, animate, frames=frames)
    anim.save('gifs/ca_tot.gif', fps=fps)