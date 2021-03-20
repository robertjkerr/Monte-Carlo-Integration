# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:50:32 2021

@author: Robert Kerr
"""

import numpy as __np




def integrate(f,n,lims,start=None):
    if start == None:
        start = __np.zeros(len(lims))
    
    
        