import math
from scipy.optimize import fsolve

#整体思路，在椭圆弧附近取x值，并推算出椭圆弧旁边两条曲线对应的x,y值，简单地说就是试算椭圆弧上的x

#迭代收敛条件，输入的y1值经迭代后基本不变

maxCounts=1000    #最大迭代次数
iterDirection=-1    #迭代方向，-1：左，1：右
step=iterDirection*0.01    #迭代步长
err=0.01   #迭代误差限值

y1=8630.57

   #指定高度

#关键参数1：
x1_est=-17612.71

    #x1估计值（决定收敛到外弧还是内弧）

#关键参数2：
x=-16106.44

x=x+5.0
    #圆弧上的x值，x初始“步”（距离太远可能导致不收敛）

y=39750*math.sqrt(1-x**2/16500**2)
dy=39750*(0.5)*(1-x**2/16500**2)**(-0.5)*(-2*x/16500**2)

#i[0]=>x1
#i[1]=>y1
#i[2]=>x
#i[3]=>y
#i[4]=>dy

def func(i):
    #x, y, z = i[0], i[1], i[2]
    return [
            (i[0]-x)**2 + (i[1] -y)**2-1500**2,
            dy*(i[1]-y)/(i[0]-x)+1
           ]
#限定象限    
r = fsolve(func,[x1_est, y1])
print(r[0])
print(r[1])

count=0


while (abs(y1-r[1]) > err):
    x=x+step
    y=39750*math.sqrt(1-x**2/16500**2)
    dy=39750*(0.5)*(1-x**2/16500**2)**(-0.5)*(-2*x/16500**2)
    r = fsolve(func,[x1_est, y1])
    count = count + 1
    print('迭代次数：')
    print(count)
    print('迭代x1结果：')
    print(r[0])
    print('迭代y1结果：')
    print(r[1])
    if count>maxCounts:
        break;
    
