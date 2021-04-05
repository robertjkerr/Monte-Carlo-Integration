# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:51:40 2021

@author: Robert Kerr
"""


import mcintegrate.allocateTools as __tools
from numpy import zeros as __zeros
from mcintegrate.throwTools import boxSample as __boxSample


"""    
    `__intBoxes` integrates a set of boxes.
    'integrate' main function. Integrates full shape, or a wedge of a full shape
"""


def __intBoxes(boxes, f, boxSize, n, lims):
    totalScatter = 0
    totalFMap = 0
    
    for box in boxes:
        scatter, fMap = __boxSample(f, box, boxSize, n, lims)
        totalScatter += scatter
        totalFMap += fMap
       
    return (totalFMap/n)*(boxSize**len(lims))



def integrate(f,lims,wedge,n,boxSize,start):
    dimensions = len(lims)
    if start == None:
        start = list(__zeros(len(lims)))

    r = 0
    integral, nextIntStep = 0, -1
    
    while nextIntStep != 0:        
        boxes = __tools.allocate(wedge[1], r, dimensions, start)[wedge[0]-1]
        while boxes == []:
            r += 1
            boxes = __tools.allocate(wedge[1], r, dimensions, start)[wedge[0]-1]

        nextIntStep = __intBoxes(boxes, f, boxSize, n, lims)
        integral += nextIntStep
        r += 1

    return integral
