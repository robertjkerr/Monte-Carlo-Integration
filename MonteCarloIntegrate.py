# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 14:19:31 2021

@author: Robert Kerr

Python library for Monte Carlo numerical integration
"""

from numpy.random import uniform as __random
from numpy import array as __array
from numpy import linspace as __linspace

#Throws point randomly onto plane postioned between (ax, ay) and (bx, by)
def __throw(ax,bx,ay,by):
    x = float(__random(ax,bx,[1]))
    y = float(__random(ay,by,[1]))
    return [x,y] 

#Returns numpy array of a scatter of n throws onto a plane
def __plane(ax,bx,ay,by,n):
    plane = []
    for i in range(n):
        plane.append(__throw(ax,bx,ay,by))
    return __array(plane)

#Finds minimum and maximum of function s.t. a<=x<=b over n iterations
def __getMinMax(f,a,b,n):
    xArr = __linspace(a,b,n)
    maxi, mini = 0, 0
    for x in xArr:
        if f(x) <= mini:
            mini = f(x)
        elif f(x) >= maxi:
            maxi = f(x)
    return mini, maxi

#Checks if a thrown point sits between the function and the x-axis
def __checkFunc(f,inV):
    if inV[1] <= f(inV[0]) and inV[1] >= 0:
        return 1    #Returns 1 if above axis and below function
    elif inV[1] >= f(inV[0]) and inV[1] <= 0:
        return -1   #Returns -1 if below axis and above function
    else:
        return 0
    
#Counts how many thrown points on a plane land under the function
def __count(f,inP):
    counter, absCounter = 0, 0
    for v in inP:
        status = __checkFunc(f,v)
        counter += status
        absCounter += abs(status)
    return counter, absCounter  #absCounter is what the count would be if integrand was always positive

#Returns definite integral approximation of f between a and b with n throws.
#Total area under function is given by total plane area * number of throws under function / total number of throws
def integrate(f,a,b,n):
    mini, maxi = __getMinMax(f, a, b, n)
    plane = __plane(a,b,mini,maxi,n)
    planeArea = (b-a)*(maxi-mini)
    counter, absCounter = __count(f,plane)
    return planeArea*counter/n

