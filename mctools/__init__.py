from mctools.modules.differentiate import partial_diff, grad, direct_diff, div
from mctools.modules.integrate import integrate_func as _integrate_func
from mctools.modules.progressBar import pbar

#kwargs handling for Monte Carlo Integration function
def integrate(f,n,lims,**kwargs):
    try:
        wedge = kwargs["wedge"]
    except:
        wedge = [1,1]
    
    try:
        box_size = kwargs["box_size"]
    except:
        box_size = 1
    
    try:
        start = kwargs["start"]
    except:
        start = None 

    return _integrate_func(f,lims,wedge,n,box_size,start)
