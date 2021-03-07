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
        area += f(x)*dx + 0.5*dx*(f(x+dx)-f(x))
    return area

if __name__=='__main__':
    f=lambda x: 2*x**2*(1-x**2)**0.5+2*((1-x**2)**1.5)/3
    
    print(integrate(f, -1, 1, 1000))