# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:39:59 2021

@author: Robert Kerr

Subroutines to assist parallelisation
"""

from itertools import product as __product

"""
    `__getCombinations` gets all vectors within limits defined by extrema
    `__oneNorm` gets the one-norm of a vector
    `__getBoxes` gets all combinations of vectors within extrema that have the same one-norm
    `allocate` gets all vectors returned by __getBoxes and divides them into sublists for each core
"""

def __getCombinations(extrema):
    QList = []
    for d in extrema:
        QList.append(list(range(d[0],d[1]+1)))
    return list(__product(*QList))

def __oneNorm(start,*args):
    norm = 0
    for i in range(len(args)):
        norm += abs(args[i]-start[i])
    return norm

def __getBoxes(r, dimensions,start):
    extrema = [[-r,r] for i in range(dimensions)]
    combinations = __getCombinations(extrema)
    return [combination for combination in combinations if __oneNorm(start,*combination) == r]

def allocate(cores, r, dimensions, start):
    boxes = __getBoxes(r, dimensions, start)
    boxList = [[] for i in range(cores)]
    for b in range(len(boxes)):
        box = boxes[b]
        pool = b%cores
        boxList[pool].append(box)
    return boxList

