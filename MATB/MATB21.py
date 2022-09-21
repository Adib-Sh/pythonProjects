# This code calculates the left, right and mid point value of the Reimann sum
#=============================================================================

# Imports
import sympy as sy



def Rei_sum(f, a, b, n):
    # Checking the lower limit would be less than Higher limit
    if a > b:
        a, b = b, a
    
    # Setting dx, sumDelta and x values
    dx = (b-a)/n
    sumDelta = 0.0
    x = a
    
    # Translates the math function in argument (f)
    def function_gen(function, **kwargs):
        expr = sy.sympify(function)
        return expr.evalf(subs=kwargs)
    
    # Calculating left Reimann Sum
    for i in range(n):
        fx = function_gen(f,x=x)
        
        sumDelta += fx
        x += dx
    left = sumDelta * dx
    
    # Resetting sumDelta and setting x as the second value of a
    sumDelta = 0.0
    x = a+dx
    
    # Calculating right Reimann Sum
    for i in range(n):
        fx = function_gen(f,x=x)
        
        sumDelta += fx
        x += dx
    right = sumDelta * dx
    
    #returning the mid point value
    mid = (right + left)/2
    return mid



print(Rei_sum('x^2', 2, 4, 10))