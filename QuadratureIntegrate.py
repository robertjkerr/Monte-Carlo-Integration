# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:51:02 2021

@author: Robert Kerr

Basic quadrature numerical integration function
"""

def integrate(f,a,b,n):
    dx = (b-a)/n
    area = 0
    for i in range(n):
        x = i*dx + a
        area += f(x)*dx
    return area