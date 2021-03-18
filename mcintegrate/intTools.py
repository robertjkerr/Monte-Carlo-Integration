# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:51:40 2021

@author: RobertKerr
"""

import multiprocessing as __mp
import throwTools as __tools

#Gets number of logical cpu cores
__cores = __mp.cpu_count()


"""
    `__allocate` gets all vectors returned by __tools.getBoxes and divides them into sublists for each core
    `__intBox` integrates a box located at a vector
"""


def __allocate(r, dimensions):
    boxes = __tools.getBoxes(r, dimensions)
    boxList = [[] for i in range(__cores)]
    
    for b in range(len(boxes)):
        box = boxes[b]
        pool = b%__cores
        boxList[pool].append(box)
        
    return boxList

def __intBoxes(boxes, f, boxSize, n, lims):
    totalScatter = 0
    totalFMap = 0
    
    for box in boxes:
        scatter, fMap = __tools.boxSample(f, box, boxSize, n, lims)
        
        totalScatter += scatter
        totalFMap += fMap
       
    return (totalFMap/n)*(boxSize**len(lims))


#pool = __mp.pool(processes=__cores)

