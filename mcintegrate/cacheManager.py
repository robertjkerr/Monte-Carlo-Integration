# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:40:13 2021

@author: Robert Kerr

Caching subroutines for recording the absolute limits (which are computationally heavy to determine) for a given set of limits

References functions by their [modified] bytecode
"""

import pickle as __pickle

__testType = lambda l: isinstance(l,int) or isinstance(l,float)
__cacheLoc = lambda f: 'mcintegrate/bin/limitsCache/' + f + '.pkl'

"""
    `createLimitCode` creates a code associated with a limit.
    Code is comprised of a spaceless string of limits (if number) and modified bytecode (if limit is a function)
"""

def createLimitCode(lims):
    limCode = ''
    for d in lims:
        for l in d:
            if __testType(l):
                limCode+=str(l)
            else:
                limCode+=str(l.__code__.co_code)
    return limCode.replace('\\x','').replace('|','_').replace('0','').replace('d','')


"""
    `tryLimitCache` checks if a limit is already in the cache
    `writeCache` creates a pickle file in cache containing absolute limits binary
    `readCache` reads the absolute limit data associated with a limit code

"""

def tryLimitCache(limCode):
    try:
        limFile = open(__cacheLoc(limCode),'rb')
        limFile.close()
        return True
    except:
        return False
    
def writeCache(limCode,absLims):
    limFile = open(__cacheLoc(limCode),'x')
    limFile.close()
    limFile = open(__cacheLoc(limCode),'wb')
    __pickle.dump(absLims,limFile)
    limFile.close()
    
def readCache(limCode):
    limFile = open(__cacheLoc(limCode),'rb')
    absLims = __pickle.load(limFile)
    limFile.close()
    return absLims
    
    
