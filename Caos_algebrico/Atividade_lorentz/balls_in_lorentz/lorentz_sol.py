#################################################################
# import modules
from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt

#################################################################
# equation constants
a = 10
b = 8/3
c = 28

# iterations
N = 10000
dt = 0.01

# config for animation
frames = 300
fps = 40
mksize = 0.2

# possible colors
colors = ['red', 'blue', 'green', 'yellow', 'black']

##################################################################

class particle:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def dx(self, x, y, z):
        # equation for dx/dt
        return (a*(y - x)) * dt

    def dy(self, x, y, z):
        # equation for dy/dt
        return (x*(c - z) - y) * dt

    def dz(self, x, y, z):
        # equation for dz/dt
        return (x*y - b*z) * dt

    def update(self):
        x = self.x
        y = self.y
        z = self.z
        self.x = self.x + self.dx(x, y, z)
        self.y = self.y + self.dy(x, y, z)
        self.z = self.z + self.dz(x, y, z)

def get_paths(particles, N):

    x, y, z = [], [], []

    for i in range(0, len(particles)):

        x.append(np.zeros(N))
        y.append(np.zeros(N))
        z.append(np.zeros(N))

        for j in range(0, N):
            particles[i].update()
            x[i][j] = particles[i].x
            y[i][j] = particles[i].y
            z[i][j] = particles[i].z

    return x, y, z
        
#################################################################

if __name__ == '__main__':
     
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    p1 = particle(.1, .1, .1)
    p2 = particle(.2, .2, .2)
    particles = [p1, p2]

    x, y, z = get_paths(particles, N)

    def animate(i):
        for j in range(0, len(particles)):
            ax.scatter(x[j][:i], y[j][:i], z[j][:i], color=colors[j], s=mksize)

    anim = FuncAnimation(fig, animate, frames=frames)
    anim.save('path.gif', fps=fps)

    plt.show()