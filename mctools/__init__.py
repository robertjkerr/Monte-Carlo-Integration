from mctools._differentiate import partialDiff, grad, directDiff
from mctools._integrate import integrate
from mctools._walk import walk as _walkAlg
import sys as _sys

def walk(start,delta,iters):
    _sys.setrecursionlimit(iters**2)
    return _walkAlg(start,delta,iters)
