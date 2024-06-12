
from math import exp, sin, cos
#f3 = open("data2.dat", "w")			*instead of creating lists, if file is required to be created for plotting
def f(x,y):
	return -0.5*exp(x/2)*sin(5*x) + 5*exp(x/2)*cos(5*x) + y		#given differential equation
	
x0 = 0.0
y0 = 0.0

x = x0
y = y0

xlist = [x0]
ylist = [y0]

xf = 5
n = 100

h = (xf - x0)/100

#implementing euler method to find the solution
for i in range(n):
	x = x + h
	y = y + f(x,y)*h
	#print(x,y,file = f3)		*instead of creating lists, if file is required to be created for plotting
	xlist.append(x)
	ylist.append(y)
	
	
#f3.close()		*instead of creating lists, if file is required to be created for plotting

print ("X: ", xlist)
print ("Y: ", ylist)
