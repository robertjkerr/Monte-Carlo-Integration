"""
Single threaded example program using mcintegrate
"""

import mcintegrate as mc
from time import time

#Function to be integrated
def f(*q):
    return q[0]**2+q[1]**2+q[2]**2

#Setup limits
def lim1(*q):
    return -(1 - q[0]**2)**0.5
def lim2(*q):
    return (1 - q[0]**2)**0.5
def lim3(*q):
    return -(1 - q[0]**2 - q[1]**2)**0.5
def lim4(*q):
    return (1 - q[0]**2 - q[1]**2)**0.5

#Limits resemble a sphere of unit radius. Note that the limits in the n-th pair must have maximum n dependent variables
lims = [[-1,1], [lim1,lim2], [lim3,lim4]]

if __name__ == '__main__':
    t0 = time()
    integral = mc.integrate(f,10000,lims,boxSize=0.5)
    print(integral,time()-t0)