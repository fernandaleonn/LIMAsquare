import numpy as np

from matplotlib import pyplot as plt
from celluloid import Camera
from IPython.display import HTML
from sympy import symbols, Function, Eq, Derivative, dsolve, solve

def my_sum(x, y):
    """A function that sums. """
    return x+y

def my_mul(x, y):
    """A function that multiply. """
    return x*y


def sistema(matriz):

    """Dada un lista de listas, regresa un sistema de ecuaciones diferenciales."""

    t = symbols('t')

    x, y = symbols('x y', cls=Function)

    eq1 = Eq(Derivative(x(t), t), matriz[0][0]*x(t) + matriz[0][1]*y(t))

    eq2 = Eq(Derivative(y(t), t), matriz[1][0]*x(t) + matriz[1][1]*y(t))

    sols = dsolve((eq1, eq2))

    return sols[0].rhs, sols[1].rhs


def saludo(persona):
    """A function that says hi to you."""
    return "¡Hola, " + persona 


class NoFunction(Exception):
    """Exception to raise when argument funtion is not a logistic map, dyadic map or tent map"""
    pass
def fd(x):
    if 0<x<0.5:
        return 2*x
    else:
        return 2*x-1
def ft(x,par):
    return par*min(x,x-1)
def fl(x,par):
    return par*x*(1-x)

def diagrama(x0, it, color1, color2, funcion, *par):    
    def f(x):
        if funcion=='dyadic map':
            return fd(x)
        elif funcion=='tent map':
            return ft(x,*par)
        elif funcion=='logistic map':
            return fl(x,*par)
        else:
            raise NoFunction       
    fig, ax = plt.subplots()
    camera = Camera(fig)
    x = [x0]
    y = [x0]
    s = np.arange(0, 1, 0.01)
    fs=[]
    
    for k in range(len(s)):
       fs.append(f(s[k]))
    
    for i in range(it):
        x.append(x[2*i])
        x.append(f(x[2*i]))
        y.append(f(y[2*i]))
        y.append(f(y[2*i]))
        ax.plot(x, y, color=color2)
        ax.plot(s, s, color='black')
        ax.plot(s,fs) 
        camera.snap()
    return camera.animate()

# anim = diagrama(.2, 10, 'green', 'red', 'tent map', 2.5)

# HTML(anim.to_html5_video())
