'''
11.12.23
Root Finding by Newton Rhapson
'''

from math import *
def f(x):
	y=x*x-2*exp(-x)
	return (y)
def derivative(x):
	y1= 2.0*x+2*exp(-x)
	return (y1)

x0=float(input("Enter value:"))
x=x0
h=-(f(x))/(derivative(x))
while abs(h)>=0.001:
	if f(x)==0:
		print("Program Terminated")
		break
	h=-(f(x))/(derivative(x))
	x=x+h
	
print (x)


