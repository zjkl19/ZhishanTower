import math
from scipy.optimize import fsolve

x=-16000

y=39750*math.sqrt(1-x**2/16500**2)

dy=39750*(0.5)*(1-x**2/16500**2)**(-0.5)*(-2*x/16500**2)

print(y)
print(dy)

x1=-14491

#i[0]=>x1
#i[1]=>y1
#i[2]=>x
#i[3]=>y
#i[4]=>dy

def func(i):
    #x, y, z = i[0], i[1], i[2]
    return [
            (i[0]-i[2])**2 + (i[1] -i[3])**2-1500**2,
            i[4]*(i[1]-i[3])/(i[0]-i[2])+1,
            i[3]-(39750*math.sqrt(1-i[2]**2/16500**2)),
            i[4]-(39750*(0.5)*(1-i[2]**2/16500**2)**(-0.5)*(-2*i[2]/16500**2)),
            i[0]-(x1)
           ]
#限定象限    
r = fsolve(func,[x1, 25000,-13000,9,1])
print(r)
