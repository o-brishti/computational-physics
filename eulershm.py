#simulating the motion of a damped harmonic oscillator using the euler method
from matplotlib import pyplot as plt

#define a function f(x, t) representing the force acting on the body
def f(x,t):			
	return -(k*x)

#initial conditions for position x0, velocity v0, and time t0
x0 = 10 
v0 = 0		

a = 0

#define the final time tf and the time step dt
t0 = 0
tf = 20
dt = 0.01

x = x0
v = v0
t = t0

k = 1
m = 2

#initialize lists to store positions, velocities, and times
xlist = [x]
vlist = [v]
tlist = [t]

#calculate number of steps
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









