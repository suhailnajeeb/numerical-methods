from sympy import Symbol, Derivative
from sympy.solvers import solve

x = Symbol('x')
y = Symbol('y')
h = Symbol('h')

f = 2*x**2 - y + 3*x*y
values = (2,3)

def printline(): print('---------------------------------------------------------------------------------------')

def steep_step(f, values, x, y, h):
    (xi, yi) = values
    dfdx = Derivative(f,x).doit().evalf(subs = {x:xi, y:yi})
    dfdy = Derivative(f,y).doit().evalf(subs = {x:xi, y:yi})
    xnew = xi + dfdx*h
    ynew = yi + dfdy*h
    g = f.subs(x, xnew)
    g = g.subs(y,ynew)
    dgdh = Derivative(g,h).doit()
    H = solve(dgdh, h)[0]
    xnew = xi + dfdx*H
    ynew = yi + dfdy*H
    return (xnew, ynew)

def steep_step_verbose(f, values, x, y, h):
    (xi, yi) = values
    dfdx = Derivative(f,x).doit()
    print('df/dx: ' + str(dfdx))
    dfdx = dfdx.evalf(subs = {x:xi, y:yi})
    print('df/dx @ ' + str(values) + ': ' + str(dfdx))
    dfdy = Derivative(f,y).doit()
    print('df/dy: ' + str(dfdy))
    dfdy = dfdy.evalf(subs = {x:xi, y:yi})
    print('df/dy @ ' + str(values) + ': ' + str(dfdy))
    xnew = xi + dfdx*h
    print('x = ' + str(xnew))
    ynew = yi + dfdy*h
    print('y = ' + str(ynew))
    g = f.subs(x, xnew)
    g = g.subs(y,ynew)
    print('g(h) = ' + str(g))
    dgdh = Derivative(g,h).doit()
    print("g'(h) = " + str(dgdh))
    H = solve(dgdh, h)
    print('Solutions of h: ' + str(len(H)))
    H = H[0]
    print('h* = ' + str(H))
    xnew = xi + dfdx*H
    ynew = yi + dfdy*H
    print('(x,y) = ' + str((xnew, ynew)))
    return (xnew, ynew)

printline()
print('Iteration 1: ')
values = steep_step_verbose(f, values, x, y, h)
printline()
print('Iteration 2: ')
values = steep_step_verbose(f, values, x, y, h)
(xi, yi) = values
Y = f.evalf(subs = {x:xi, y:yi})
print('Height on the mountain: ' + str(Y))
printline()