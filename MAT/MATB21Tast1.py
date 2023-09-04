# This code calculates the left, right and mid point value of the Reimann sum
#=============================================================================
# Task 1 Part 1
# Imports
import sympy as sy

# Translates the math function in argument (f)
def function_gen(function, **kwargs):
    expr = sy.sympify(function)
    return expr.evalf(subs=kwargs)

def Rei_sum(f, a, b, n):
    # Checking the lower limit would be less than Higher limit
    if a > b:
        a, b = b, a
    
    # Setting dx, sumDelta and x values
    dx = (b-a)/n
    sumDelta = 0.0
    x = a
    

    
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



print(Rei_sum('x^2', -2, 1, 10))

# Task 1 Part 2
import scipy.integrate as integrate
import matplotlib.pyplot as plt

res = integrate.quad(lambda x : x**2,-2,1)[0]
diff = []
n = 50
for i in range (1,n):    
    diff.append(Rei_sum('x^2', -2, 1, i)-res)

x = list(range(1,n))
y = diff


fig = plt.figure()
plt.plot(x, y, linestyle='-', marker='o', color='b')
plt.xlabel('Error')
plt.ylabel('n')
plt.title('Rei_sum error graph')

# Task 1 Part 3
def g(t):
    return (4*(t**2)+9*(t**4))**(1/2)

D = abs(Rei_sum(g,-2,1,10000)-integrate.quad(g,-2,1)[0])

print(D)