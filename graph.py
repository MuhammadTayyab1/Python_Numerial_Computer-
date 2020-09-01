import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x) - 1.3*x

rootx=[2,2.2,2.5,2.8]
rooty=[-1,0,-0.5,1]
x=np.linspace(-2,3)
plt.title('Bisection')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')

plt.scatter(rootx,rooty,color='r',marker='+')
plt.plot(x,f(x))

plt.show()
