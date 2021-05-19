"""
Single threaded example program using mcintegrate
"""

import mctools as mc
from time import time

#Function to be integrated
f = lambda *q: q[0]**2+q[1]**2+q[2]**2

#Setup limits
lim1 = lambda *q: -(1 - q[0]**2)**0.5
lim2 = lambda *q: (1 - q[0]**2)**0.5
lim3 = lambda *q: -(1 - q[0]**2 - q[1]**2)**0.5
lim4 = lambda *q: (1 - q[0]**2 - q[1]**2)**0.5

#Limits resemble a sphere of unit radius. Note that the limits in the n-th pair must have maximum n dependent variables
lims = [[-1,1], [lim1,lim2], [lim3,lim4]]

if __name__ == '__main__':
    t0 = time()
    integral = mc.integrate(f,1000,lims,boxSize=0.5)
    print(integral,time()-t0)
