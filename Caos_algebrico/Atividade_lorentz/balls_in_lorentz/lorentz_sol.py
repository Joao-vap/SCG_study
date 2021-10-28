#################################################################
# import modules
from mpl_toolkits import mplot3d
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


#################################################################

if __name__ == '__main__':
     
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    p1 = particle(.1, .1, .1)
    p2 = particle(.01, .01, .01)
    particles = [p1, p2]

    for i in range(0, len(particles)):

        x = np.zeros(N)
        y = np.zeros(N)
        z = np.zeros(N)

        for j in range(0, N):
            particles[i].update()
            x[j] = particles[i].x
            y[j] = particles[i].y
            z[j] = particles[i].z
        
        ax.plot(x, y, z, color = colors[i], label = 'particle ' + str(i), linewidth = 0.1)

    plt.show()