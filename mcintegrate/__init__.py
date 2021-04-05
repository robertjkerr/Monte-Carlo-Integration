# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:50:32 2021

@author: Robert Kerr
"""

from mcintegrate.intTools import integrate as __integrate
from mcintegrate.diffTools import partialDiff, grad, differentiate

def integrate(f,n,lims,**kwargs):
    try:
        wedge = kwargs["wedge"]
    except:
        wedge = [1,1]
    
    try:
        boxSize = kwargs["boxSize"]
    except:
        boxSize = 1
    
    try:
        start = kwargs["start"]
    except:
        start = None

    return __integrate(f,lims,wedge,n,boxSize,start)

