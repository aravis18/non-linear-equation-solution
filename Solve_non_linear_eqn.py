#%%
from scipy.optimize import fsolve
import math
#%%
def equations(p):
    x, y = p
    return (x*y+ 50.45*x - 50.45, x*y - 1112.6*x**2 + 2225.2*x - 1112.6)
#%%
x, y =  fsolve(equations, (1, 1))
#%%
print (equations((x, y)))
# %%
print((x,y))
# %%
