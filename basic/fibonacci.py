# -*- coding: utf-8 -*-

n = int(input('Enter the number'))

n1 = 0
n2 = 1
c = 0
print('Fibonacci series are:')
if n==1:
    print(n1)
else:
    while c<n:
        print(n1, end = ',')
        nn = n1 + n2
        n1 = n2
        n2 = nn
        c += 1