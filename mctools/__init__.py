from mctools.modules.differentiate import partialDiff, grad, directDiff
from mctools.modules.integrate import integrateFunc as _integrateFunc
from mctools.modules.progressBar import pbar

#kwargs handling for Monte Carlo Integration function
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

    return _integrateFunc(f,lims,wedge,n,boxSize,start)
