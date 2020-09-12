from sympy import Symbol
x = Symbol('x')

f = 0.2 + 25*x - 200 * x**2 + 675 * x**3 - 900 * x**4 + 400 * x**5

a = 0.0
b = 0.8
n = 3

def simp38(f, a, b, n = 3):
    h = (b-a)/n
    print('h = %.4f'% h)
    x0 = a
    print('x0 = %.4f'% x0)
    x1 = a + h
    print('x1 = %.4f'% x1)
    x2 = a + 2*h
    print('x2 = %.4f'% x2)
    x3 = a + 3*h
    print('x3 = %.4f'% x3)
    fx0 = f.subs(x, x0)
    print('f(x0) = %.4f'% fx0)
    fx1 = f.subs(x, x1)
    print('f(x1) = %.4f'% fx1)
    fx2 = f.subs(x, x2)
    print('f(x2) = %.4f'% fx2)
    fx3 = f.subs(x, x3)
    print('f(x3) = %.4f'% fx3)
    I = (b-a)/8*(fx0+ 3*fx1 + 3*fx2 + fx3)
    print("Integral using Simpson's 3/8 rule from %.1f to %.1f = %.4f" % (a, b, I))
    return I

def simp13(f, a, b, n = 2):
    h = (b-a)/n
    print('h = %.4f'% h)
    x0 = a
    print('x0 = %.4f'% x0)
    x1 = a + h
    print('x1 = %.4f'% x1)
    x2 = a + 2*h
    print('x2 = %.4f'% x2)
    fx0 = f.subs(x, x0)
    print('f(x0) = %.4f'% fx0)
    fx1 = f.subs(x, x1)
    print('f(x1) = %.4f'% fx1)
    fx2 = f.subs(x, x2)
    print('f(x2) = %.4f'% fx2)
    I = (b-a)/6*(fx0+ 4*fx1 + fx2)
    print("Integral using Simpson's 1/3 rule from %.1f to %.1f = %.4f" % (a, b, I))
    return I