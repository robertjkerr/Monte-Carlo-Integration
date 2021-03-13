# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:59:37 2021

@author: Robert Kerr

Function initialisation subroutines. Finds absolute limits given limit function
"""

from numpy import linspace as __linspace
from itertools import product as __product
import mcintegrate.cacheManager as __cacheManager


"""
    `__testType` checks if input is number or (by implication) a function
    `throwCheck` tests if throw is inside limits
    `__getQProduct` finds all combinations of elements in QList
    `__getMax` finds the maximum and limit function allows given its dependencies
    `__getMin` same as __getMax but finds minimum
    `__findAbsLimits` finds absolute maximum each limit returns
    
"""

__testType = lambda l: isinstance(l,int) or isinstance(l,float)

def throwCheck(throw,lims):
        d = len(lims)
        for i in range(d):#Check each dimension
            l = lims[i]
            if __testType(l[0]):#Find lower limit
                a = l[0]
            else:
                a = l[0](*throw)
            
            if __testType(l[1]):#Find upper limit
                b = l[1]
            else:
                b = l[1](*throw)
            
            if throw[i]>=b or throw[i]<=a:#Check limits
                return False
        return True


def __getQProduct(d,QList,lims):#Returns list of all positions within limits
        diff = len(lims)-len(QList)
        if diff != 0:
            n = len(QList[0])
            for e in range(diff):
                QList.append(__linspace(0,0,n))
            
        fullQProduct = list(__product(*QList))
        QProduct = []
        for q in fullQProduct:
            if throwCheck(q,lims):
                
                QProduct.append(q)
        return QProduct
    
def __getMax(n,d,lim,absLims,lims):
    QList = [__linspace(*absLim,n) for absLim in absLims]
    QProduct = __getQProduct(d,QList,lims)
    maxi = lim(*QProduct[0])
        
    for args in QProduct:
        if lim(*args) > maxi:
            maxi = lim(*args)
                
    return maxi

def __getMin(n,d,lim,absLims,lims):
    QList = [__linspace(*absLim,n) for absLim in absLims]
    QProduct = __getQProduct(d,QList,lims)
    mini = lim(*QProduct[0])
        
    for args in QProduct:
        if lim(*args) < mini:
            mini = lim(*args)
                
    return mini

def __findAbsLims(lims,n):
    absLims = []
    dims = len(lims)
    for i in range(len(lims)):
        l = lims[i]
        if __testType(l[0]):
            a = l[0]
        else:
            a = __getMin(int(n/dims),i,l[0],absLims,lims)
                
        if __testType(l[1]):
            b = l[1]
        else:
            b = __getMax(int(n/dims),i,l[1],absLims,lims)
                
        absLims.append([a,b])
    return absLims

def __checkCache(lims):
    isCached = __cacheManager.tryLimitCache(lims)
    if isCached:
        absLims = __cacheManager.readCache(lims)
        return absLims
    else:
        return None

def getAbsLims(n,lims):
    __limitCode = __cacheManager.createLimitCode(lims)
    __lims = lims
    
    #Checks if function limits have already been cached
    if __checkCache(__limitCode) == None:
        print('Finding Limits...')
        absLims = __findAbsLims(lims,n)
        __cacheManager.writeCache(__limitCode, absLims)
        print('Cached limits')
    else:
        absLims = __checkCache(__limitCode)
        print('Found limits in cache')
    
    return absLims



