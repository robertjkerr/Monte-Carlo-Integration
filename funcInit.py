# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:59:37 2021

@author: Robert Kerr

Function initialisation subroutines. Find absolute limits given limit function
"""

from numpy import linspace as _linspace
from itertools import product as _product

#Creates object contain the function, its maximum and minium between a and b over n steps
class function:
    """
        `__testType` checks if input is number or (by implication) a function
        `throwCheck` tests if throw is inside limits
        `__getQProduct` finds all combinations of elements in QList
        `__getMax` finds the maximum and limit function allows given its dependencies
        `__getMin` same as __getMax but finds minimum
        `__findAbsLimits` finds absolute maximum each limit returns
        
    """
    
    def __testType(self,l):
        return isinstance(l,int) or isinstance(l,float)
    
    def throwCheck(self,throw,lims):
        d = len(lims)
        for i in range(d):#Check each dimension
            l = lims[i]
            if self.__testType(l[0]):#Find lower limit
                a = l[0]
            else:
                a = l[0](*throw)
            
            if self.__testType(l[1]):#Find upper limit
                b = l[1]
            else:
                b = l[1](*throw)
            
            if throw[i]>=b or throw[i]<=a:#Check limits
                return False
        return True
    
    def __getQProduct(self,d,QList):#Returns list of all positions within limits
        diff = len(self.__lims)-len(QList)
        if diff != 0:
            n = len(QList[0])
            for e in range(diff):
                QList.append(_linspace(0,0,n))
            
        fullQProduct = list(_product(*QList))
        QProduct = []
        for q in fullQProduct:
            if self.throwCheck(q,self.__lims):
                
                QProduct.append(q)
        return QProduct
    
    def __getMax(self,n,d,lim,absLims):
        QList = [_linspace(*absLim,n) for absLim in absLims]
        QProduct = self.__getQProduct(d,QList)
        maxi = lim(*QProduct[0])
        
        for args in QProduct:
            if lim(*args) > maxi:
                maxi = lim(*args)
                
        return maxi
        
    def __getMin(self,n,d,lim,absLims):
        QList = [_linspace(*absLim,n) for absLim in absLims]
        QProduct = self.__getQProduct(d,QList)
        mini = lim(*QProduct[0])
        
        for args in QProduct:
            if lim(*args) < mini:
                mini = lim(*args)
                
        return mini
            
    def __findAbsLims(self,lims,n):
        absLims = []
        dims = len(lims)
        for i in range(len(lims)):
            l = lims[i]
            if self.__testType(l[0]):
                a = l[0]
            else:
                a = self.__getMin(int(n/dims),i,l[0],absLims)
                
            if self.__testType(l[1]):
                b = l[1]
            else:
                b = self.__getMax(int(n/dims),i,l[1],absLims)
                
            absLims.append([a,b])
        return absLims    
    
    def __init__(self,f,n,lims):
        self.__f = f
        self.__funcCode = f.__code__.co_code
        self.__lims = lims
        self.__absLims = self.__findAbsLims(lims,n)
        
    def getAbsLims(self):
        return self.__absLims
        
    def __call__(self,*x):
        return self.__f(*x)
        
    #Returns function bytecode for caching
    def getCode(self):
        return self.__funcCode
    


