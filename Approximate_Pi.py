# Fettet, Louis
# Approximate Pi Project
# 9/20/2011

from math import pi, fabs
from random import uniform

def getPoint():
    """
    Returns a random point in first quandrant.
    >>> (x,y)=getPoint()
    >>> x*x <= 1 and y*y <= 1 
    True
    """
    x = uniform(0,1)
    y = uniform(0,1)
    return (x, y)

def withinCircle(x, y):
    """
    Determine whether the point (x,y) is within the unit circle
    centered at (0,0)
    >>> withinCircle(0.5,0.5)
    True
    >>> withinCircle(1,0.5)
    False
    """
    return (x * x) + (y * y) <= 1
        
def approxPi(iterations, verbose):
    """
    This function accepts a number which will be the number of iterations
    to run.  And it returns its approximation of pi obtained after that
    number of iteration.
    The second parameters (verbose) indicates whether to print something 
    during the simulation.
    The following test ensures that the function returns an acceptable
    approximation.
    >>> fabs(approxPi(1000,False)-pi) < 0.5
    True
    """
    hits = 0
    for i in range (iterations):
        (rx, ry) = getPoint()
        if withinCircle(rx,ry):
            hits += 1
            if (verbose):
                print ((rx, ry),("  HIT  "), (4 * (hits / iterations)))
        else:
            if (verbose):
                print ((rx, ry),("  MISS  "), (4*(hits / iterations)))
    return 4 *(hits / iterations)


def main():
    import doctest
    print ('Testing... please wait...')
    doctest.testmod()

if __name__ == '__main__':
    main()
