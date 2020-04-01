import numpy as np

a0 = 3.56
a1 = 1.4859
a2 = 2.025

x = np.array([1,2,3,4,5])
y = np.array([7.7, 14.5, 26, 40, 62])

xm = np.mean(x).round(4)
ym = np.mean(y).round(4)

print('mean of x: ' + str(xm))
print('mean of y: ' + str(ym))

st = lambda yi : np.square(yi - ym).round(4)
sr = lambda xi,yi : np.square(yi-a0-a1*xi-a2*np.square(xi)).round(4)

def printline(): print('----------------------------------------------------------------------')

printline()
print('xi\t\tyi\t\t(yi-ym)^2\t(yi-a0-a1xi-a2xi^2)^2')
for i in range(len(x)):
    printline()
    print(str(x[i]) + '\t\t' + str(y[i]) + '\t\t' + str(st(y[i])) + '\t\t' + str(sr(x[i],y[i])))