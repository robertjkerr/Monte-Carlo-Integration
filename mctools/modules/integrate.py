# -*- coding: utf-8 -*-
"""
@author: Robert Kerr

Monte Carlo Integration function 
"""

import numpy as _np
from itertools import product as _product
from functools import lru_cache as _lru_cache

"""
Allocation subroutines. Assists with parallelisation.
"""


#Gets all vectors within limits defined by extrema.
def _get_combinations(extrema, onenorm, prev_q=None):
    dims = len(extrema)
    
    if dims == 1:
        this_range = range(*extrema[0])
        
        if prev_q == None:
            if onenorm in this_range:
                yield onenorm
            if -onenorm in this_range:
                yield -onenorm
        else:
            if onenorm in this_range:
                yield (*prev_q, onenorm)
            if -onenorm in this_range:
                yield (*prev_q, -onenorm)
    
    else:
        lower_lim = max(extrema[0][0], -onenorm)
        upper_lim = min(extrema[0][1], onenorm)
        
        for q in range(lower_lim, upper_lim+1):
            if prev_q == None:
                this_q = [q]
            else:
                this_q = [*prev_q, q]
                
            yield from _get_combinations(extrema[1:], onenorm-abs(q), this_q)

#gets all combinations of vectors within extrema that have the same one-norm.
def _get_boxes(r0, dimensions,start):
    extrema = lambda r: tuple([(-r+start[d],r+start[d]) for d in range(dimensions)])
    boxes = tuple(_get_combinations(extrema(r0), r0))
    return boxes

#gets all vectors returned by _get_boxes and divides them into sublists for each core.
def _allocate(cores, r, dimensions, start):
    boxes = _get_boxes(r, dimensions, start)
    box_list = [[] for i in range(cores)]
    
    b = 0
    for box in boxes:
        pool = b%cores
        box_list[pool].append(box)
        b += 1
   
    if box_list == []:
        return _allocate(cores, r+1, dimensions, start)
    else:
        return tuple(box_list)


"""
Throw tools. Used for Monte Carlo random throwing.
"""

#Checks if input is a number or (by assumption) a function.
def _test_type(l):
    return isinstance(l,int) or isinstance(l,float)

#Checks if throw is within limits.
def _throw_check(throw,lims):
    d = len(lims)
    for i in range(d):#Check each dimension
        l = lims[i]
        if _test_type(l[0]):#Find lower limit
            a = l[0]
        else:
            a = l[0](*throw)
        
        if _test_type(l[1]):#Find upper limit
            b = l[1]
        else:
            b = l[1](*throw)
        
        if throw[i]>=b or throw[i]<=a:#Check limits
            return False 
    return True 

#Returns a scatter of throws. Each row is a throw.
def _scatter(corner, box_size, dimensions, n):
    throw = lambda : box_size * (_np.random.rand(dimensions) + _np.array(corner))
    return (throw() for i in range(n))

#Returns all throws in a scatter that are within the limits.
def _filter_scatter(scatter, lims):
    check = lambda throw: _throw_check(throw, lims)
    filtered_scatter = filter(check, scatter) 
    return filtered_scatter 

#Takes a selection of boxes, scatters over them and filters the throws.
def _filter_boxes(boxes, box_size, n, lims):
    adj_n = round(n * box_size)
    make_scatter = lambda box: _scatter(box, box_size, len(lims), adj_n)
    filt = lambda box: _filter_scatter(make_scatter(box), lims)
    num_throws = adj_n*len(boxes)
    filtered_throws = map(filt, boxes)

    parsed_throws = []
    for part in filtered_throws:
        for throw in part:
            parsed_throws.append(throw)

    return tuple(parsed_throws), num_throws


"""
Integration subroutines. Main functions for integrating.
"""

#Main algorithm. Expands from start and throws scatters and filters them until the limits have been engulfed.
def _converge(lims, wedge, n, box_size, start, r, total_throws, total_boxes):
    dimensions = len(lims)
    diff = (_np.array(start)/box_size).astype(int)
    boxes = _allocate(wedge[1], r, dimensions, diff)[wedge[0]-1]
    
    num_boxes = len(boxes)
    filtered_throws, num_throws = _filter_boxes(boxes, box_size, n, lims)
    if filtered_throws != ():
        return filtered_throws + _converge(lims, wedge, n, box_size, start, r+1, total_throws+num_throws, total_boxes+num_boxes)
    else:
        return filtered_throws, total_throws+num_throws, total_boxes+num_boxes

#maps all the filtered throws and finds the integral.
def integrate_func(f, lims, wedge, n, box_size, start):
    if start == None:
        start = _np.zeros(len(lims))
    g = lambda throw: f(*throw)
    try:
        get_throws = _converge(lims,wedge,n,box_size,start,0,0,0)
        l = len(get_throws)
        throws = tuple([throw for throw in get_throws[:(l-3)]])
        total_throws, total_boxes = get_throws[l-2], get_throws[l-1]
        fMap = map(g, throws)
        if total_throws != 0:
            return (total_boxes*box_size**len(lims))*sum(fMap)/total_throws
        else:
            return 0
    except RecursionError:
        print('Suspected recursion depth exceeded. Try increasing "box_size"')
