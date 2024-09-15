'''
Date: 11.12.23
Root Finding by Bisection Method
'''

def f(x):
	return x**3-5.816*x**2+9.632*x-7.632

a=float(input("Enter lower limit:"))
b=float(input("Enter upper limit:"))
tol=float(input("Enter tolerance:"))

while f(a)*f(b)>0:
	print("No root in this interval")
	break
	
while abs(b-a)>=tol:
	xm=0.5*(a+b)
	if f(xm)==0:
		print("root=",xm)
		break
	if f(a)*f(xm)<0:
		b=xm
	else:
		a=xm
print("root=",(a+b)*0.5)
