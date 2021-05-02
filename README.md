# Python Monte Carlo Tools

Library with useful functions for numerical mathematics and physics.

Scaled to support x dimensions

#### Monte Carlo Integration

To use, call `mctools.integrate(f, n, lims, **kwargs)`, where `f` is a function of x arguments, `n` is the number of iterations per box (serves as minimum number of iterations), and `lims` are the limits of the integral (functions or numbers). 

List of `kwargs`
 - `start` is the x-dimensional coordinate for where the integration begins. The algorithm expands around this point until the shape defined by the limits is encapsulated and the integral converges. Is by default at the origin.
 - `wedge` is the segment of the shape which is integrated. For example, `wedge=[3,8]` means the function will only integrate the 'third eighth' of the shape. This makes multiprocessing easier as the integral job can be spread over several threads. By default, `wedge=[1,1]`, and may be defined as `wedge=[segment, total number of segments]`. Note that if multiple segments are used, the total integral is sum of the integral of each wedge e.g. `full integral = integrate(..., wedge=[1,2]) + integrate(..., wedge=[2,2])`
 - `boxSize` is by default `1`. Details the size of the box which is integrated on each iteration.

#### Numerical differentiation

Numerical multidimensional derivative functions are included as well:
 - `partialDiff(f, position, axis, dimensions, delta)` gets partial derivative of function `f` at `position` along `axis`th direction, with `dimensions` total number of dimensions and step-size `delta`
 - `grad(f, position, dimensions, delta)` gets grad of function `f` with similar arguments to `partialDiff`
 - `directDiff(f, position, dimensions, delta)` gets directional derivative of `f`

#### Progress bar

Simple console progress bar

 - `mctools.pbar(iters, totalIters)` prints a progress bar with percentage `iters/totalIters`