# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 13:20:00 2019

@author: Neeraj Shetty
"""

print(__name__)
def main1():
    print('Hello World')
    otherfunction()
    
def otherfunction():
    print('This is another function')
    
if(__name__== '__main__'):
    main1()