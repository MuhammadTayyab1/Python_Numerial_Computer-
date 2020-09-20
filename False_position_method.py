import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x) - 1.3*x

alst=list()
blst=list()
rootlst=list()
itrlst=list()

def RegulaFalsi(a,b, tol):
    i=0
    while (i<20):
        Xr= (a*f(b) - b*f(a)) / (f(b)-f(a))
        if(Xr==0 or np.abs(f(Xr)) < tol):
            break
        if(f(a) *f(Xr)) < 0:
            b=Xr
        else:
            a=Xr
        i+=1

        itrlst.append(i)
        alst.append(a)
        blst.append(b)
        rootlst.append(Xr)

    return i,Xr

ite, root = RegulaFalsi(-3,3,0.0001)
print("No of iterations to find the root ",ite)
print("Root for given equation ",root)

rfData={
    'Itr': itrlst,
    'a': alst,
    'b':blst,
    'root': rootlst
}

mytable  = pd.DataFrame(rfData)
x= mytable
print(x)

x = np.linspace(-3,3)
plt.grid()

plt.title('Rugula Falsi Method')
plt.xlabel('X-Axis')
plt.ylabel("Y-Axis")
plt.scatter(root,f(root),color='r')

plt.plot(x,f(x))
