# Fettet, Louis
# Triangles Project
# 9/27/11

def drawLeftTriangle(height):
    """
    Draws a right-angle triangle of height lines with the right angle on the left.
    >>> drawLeftTriangle(2)
    T
    TT
    >>> drawLeftTriangle(5)
    T
    TT
    TTT
    TTTT
    TTTTT
    """
    for i in range(abs(height)):
        i += 1
        print (i * "T")

def drawRightTriangle(height):
    """
    Draws a right-angle triangle of height lines with the right angle on the right.
    >>> drawRightTriangle(2)
     T
    TT
    >>> drawRightTriangle(5)
        T
       TT
      TTT
     TTTT
    TTTTT
    """
    for i in range(abs(height)):
        i += 1
        for j in range (i):
            j = " "
        print(((height - i) * j) + (i * "T"))
       
def drawTriangle(height):
    """
    Draws a right-angle triangle of height lines with the right angle on the right
    or on the left, according to the sign of the parameter height.
    >>> drawTriangle(5)
    T
    TT
    TTT
    TTTT
    TTTTT
    >>> drawTriangle(-5)
        T
       TT
      TTT
     TTTT
    TTTTT
    """
    if (height) > 0:
        drawLeftTriangle(height)
    else:
        drawRightTriangle(-height)

def main ():
    import doctest
    print ('Testing... please wait...')
    doctest.testmod()

if __name__ == '__main__':
    main()
