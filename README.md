Python library with Monte Carlo integration function.

Scaled to support x dimensions

To use, call mcintegrate.integrate(f,n,lims,start), where `f` is a function of x arguments, `n` is the number of iterations and `lims` are the limits of the integral (functions or numbers). `start` is the x-dimensional coordinate for where the integration begins. The algorithm expands around this point until the shape defined by the limits is encapsulated and the integral converges.