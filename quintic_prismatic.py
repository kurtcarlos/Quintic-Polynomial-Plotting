import numpy as np
import matplotlib.pyplot as plt

# degrees to radian converter
def mm_to_meters(d):
    m=1000
    return d/m

qi = float(input('qi = ')) # initial position
qi = mm_to_meters(qi)

vi = float(input('vi = ')) # initial velocity
vi = mm_to_meters(vi)

aci = float(input('aci = ')) # initial acceleration
aci = mm_to_meters(aci)

qf = float(input('qf = ')) # final position
qf = mm_to_meters(qf)

vf = float(input('vf = ')) # final velocity
vf = mm_to_meters(vf)

acf = float(input('acf = ')) # final acceleration
acf = mm_to_meters(acf)

ti = float(input('ti = ')) # initial time
tf = float(input('tf = ')) # final time

# Cubic
# Solve the solution for q(t) = c0 + c1*t + c2*t**2 + c3*t**3 +c4*t**4 +c5*t**5

M = [[1, ti, ti**2, ti**3, ti**4, ti**5],
      [0, 1, 2*ti, 3*ti**2, 4*ti**3, 5*ti**4],
      [0, 0, 2, 6*ti, 12*ti**2, 20*ti**3],
      [1, tf, tf**2, tf**3, tf**4, tf**5],
      [0, 1, 2*tf, 3*tf**2, 4*tf**3, 5*tf**4],
      [0, 0, 2, 6*tf, 12*tf**2, 20*tf**3]]

M = np.matrix(M)

b = [[qi], [vi], [aci], [qf], [vf], [acf]]

a = np.linalg.inv(M) * b
x = np.arange(ti,tf,0.05)

def qt(t,c0,c1,c2,c3,c4,c5):
    return c0 + c1*t + c2*t**2 + c3*t**3 +c4*t**4 +c5*t**5

y = qt(x,a[0,0],a[1,0],a[2,0],a[3,0],a[4,0],a[5,0])

plt.figure()
plt.plot(x,y,'b',linestyle='-')
plt.text(1,-1.5,'q(t) = c0 + c1*t + c2*t**2 + c3*t**3 +c4*t**4 +c5*t**5')
plt.grid(True)
plt.show()