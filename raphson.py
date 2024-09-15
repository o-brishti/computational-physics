from math import *
def f(x):
	return exp(x)*log(x) - x**2
	
def derivative(x):
	return exp(x)*log(x) + exp(x)/x - 2*x
	
x0 = 3
x = x0

h = -f(x)/derivative(x)

while abs(h)>=0.0001:
	if f(x) == 0:
		print(x)
		break
	elif derivative(x) == 0:
		print("Initial Guess is wrong")
		break
	else:  
		h = -f(x)/derivative(x)
		x = x + h 
		
print(x)
		
