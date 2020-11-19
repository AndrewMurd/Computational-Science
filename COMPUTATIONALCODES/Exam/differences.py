"""
DIFFERENCES FUNCTION
"""

import math

def f(x):                                       #function goes here
    return 

def fp(x):                                      #derivative function goes here
    return

def fD(f,h,x):                                  #centered differencen function
    return (f(x+h) - f(x))/h
    
def cD(f,h,x):                                  #forward difference function
    return (f(x+h) - f(x-h))/(2*h)

def bD(f,x,h):
    return (f(x)-(f(x-h)))/(h)

def errorD(f,fp):                               #calculating the error between prime function and any difference
    return abs(fp - f)


h = 0                                           #your h value goes here

x = 0                                           #your x value goes here

print()                                         #the difference function you want to print goes here