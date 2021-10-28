#################################################################
# import modules
import numpy as np
import matplotlib.pyplot as plt

#################################################################
# initial conditions

# vector size of x
N = 1000

# possible rs to be tested
rs = np.linspace(1,4,10000)

# list of x_n
x = np.zeros(N)
x[0] = 0.5

# list with last values of x_n
last_values = np.arange(int(N*9/10), N)

##################################################################

def iterate_in_ri(N, ri):
    """
    Iterate over the logistic curve for given r and initial conditions
    """
    for n in range(N-1):
        x[n+1] = ri*x[n]*(1-x[n])

def iterate_rs():
    """
    iterate over possible rs
    """
    for ri in rs:
        # iterate for each r
        iterate_in_ri(N, ri)
        # set unique points of convergence for each r
        gy = np.unique(x[last_values])
        # set wich r were used
        gx = ri * np.ones(len(gy))
        #plot
        plt.plot(gx, gy, 'k.', markersize=.5, alpha=0.3)


#################################################################

if __name__ == '__main__':
    iterate_rs()
    plt.show()