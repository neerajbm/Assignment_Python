# -*- coding: utf-8 -*-

def simple(p, t, r):
    si = (p*t*r)/100
    return si

p = int(input('Enter principal'))
t = int(input('Enter time'))
r = int(input('Enter rate of intrest'))
intrest = simple(p, t, r)
print('Simple intrest is', intrest)
