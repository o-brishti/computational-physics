from matplotlib import pyplot as plt

def f(x,t):			#m*(d2x/dt2)
	return -(k*x)
	
x0 = 10 
v0 = 0		#dx/dt

a = 0

t0 = 0
tf = 20
dt = 0.01

x = x0
v = v0
t = t0

k = 1
m = 2

xlist = [x]
vlist = [v]
tlist = [t]

n = int((tf - t0)/dt)

#euler method implementation
for i in range(n):

	F = f(x,t)
	a = F/m
	
	v = v + a*dt
	x = x + v*dt
	t = t + dt
	
	if x < 0:
		x = 0
		v = -v
	
	vlist.append(v)
	xlist.append(x)
	tlist.append(t)
	

plt.plot(tlist, xlist)
plt.xlabel("Time")
plt.ylabel("Position")
plt.title("Motion of a Body undergoing SHM using Euler Method")
plt.show()












