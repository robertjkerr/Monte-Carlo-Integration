"""
Example program using mcintegrate
"""

import mcintegrate as mc
import multiprocessing as mp

cpus = mp.cpu_count()

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

def integrate(segment):
    return mc.integrate(f,100,lims,boxSize=0.5,wedge=[segment,cpus])

#Segments integral into multiple wedges and then parallelised
if __name__ == '__main__':
    pool = mp.Pool(processes=cpus)
    results = [pool.apply(integrate, args=(s,)) for s in range(1,cpus+1)]
    print(sum(results))
