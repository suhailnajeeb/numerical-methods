# This code isn't optimized. I wrote it to just get the job done.

import numpy as np

'''
X1 = [4, 5, 7, 8, 9]
X2 = [3, 4, 5, 6, 5]
Y = [110, 250, 520, 860, 670]
'''
X1 = [4, 5, 7, 8, 9]
X2 = [3, 4, 5, 6, 5]
Y = [380, 1000, 3400, 6100, 7300]


x1 = 5
x2 = 7

def printline(): print('---------------------------------------------------------------------------------------')

print('Logarithmic polynomial Linear Regression on the provided data:')

printline()
print("x1\tx2\tY\tx1'\tx2'\ty'\tx1'^2\tx2'^2\tx1'x2'\tx1'y\tx2'y")
printline()

sumx1 = 0
sumx2 = 0
sumy = 0
sumx1sqr = 0
sumx2sqr = 0
sumx1x2 = 0
sumx1y = 0
sumx2y = 0

for i in range(len(Y)):
    x1 = np.log10(X1[i]).round(3)
    x2 = np.log10(X2[i]).round(3)
    y = np.log10(Y[i]).round(3)
    x1sqr = np.square(x1).round(3)
    x2sqr = np.square(x2).round(3)
    x1x2 = (x1*x2).round(3)
    x1y = (x1*y).round(3)
    x2y = (x2*y).round(3)
    sumx1 = sumx1 + x1
    sumx2 = sumx2 + x2
    sumy = sumy + y
    sumx1sqr = sumx1sqr + x1sqr
    sumx2sqr = sumx2sqr + x2sqr
    sumx1x2 = sumx1x2 + x1x2
    sumx1y = sumx1y + x1y
    sumx2y = sumx2y + x2y
    print(str(X1[i]) + '\t' + str(X2[i]) + '\t' + str(Y[i]) + '\t' + str(x1) +
    '\t' + str(x2) + '\t' + str(y) + '\t' + str(x1sqr) + '\t' + str(x2sqr) +
    '\t' + str(x1x2) + '\t' + str(x1y) + '\t' + str(x2y))

printline()

print('\t\t\t' + str(sumx1.round(3)) + '\t' + str(sumx2.round(3)) + '\t' +
str(sumy.round(3)) + '\t' + str(sumx1sqr.round(3)) + '\t' + str(sumx2sqr.round(3)) +
'\t' + str(sumx1x2.round(3)) + '\t' + str(sumx1y.round(3)) + '\t' + str(sumx2y.round(3)))

n = len(Y)

A = np.array([n, sumx1, sumx2,
    sumx1, sumx1sqr, sumx1x2,
    sumx2, sumx1x2, sumx2sqr]).reshape((3,3))

b = np.array([sumy, sumx1y, sumx2y])

a0, a1, a2 = np.linalg.solve(A,b)
a0 = 10**a0

print()
print('Solving the following equations: ')
print(A, end = '')
print('* [a0,a1,a2] =', end = '')
print(b)
print()
print('Solution to the values: a0 = %f , a1 = %f, a2 = %f '% (a0, a1, a2))

y = a0 * (x1**a1) * (x2**a2)

print()
print('Predicted value of y: %f' % y)