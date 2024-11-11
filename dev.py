import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-tf', type=int,help="tiempo final")
parser.add_argument('-pos', type=float,help="posicion inicial del objeto")
parser.add_argument('-acel', type=float,default=10,help="aceleracion del objeto")
parser.add_argument('-vel', type=float,help="velocidad inicial")
args = parser.parse_args()

print(args.acel)

def get_position(x0,t,v0,a):
    x = x0 + v0*t+a*t**2
    return x

def get_velocities(v0,a,t):
    v = v0 + a*t
    return v

dt = 5
t0 = 0
tf = args.tf

ts = [t for t in range(t0,tf,dt)]

x0 = args.pos
a = args.acel
v0 = args.vel

xs = []
vs = []
for t in ts:
    x = get_position(x0,t,v0,a)
    v = get_velocities(v0,a,t)
    xs.append(x)
    vs.append(v)

xs = np.array(xs)
vs = np.array(vs)
ts = np.array(ts)

fig,ax = plt.subplots(figsize=(6,5),dpi=150)
plt.subplots_adjust(wspace=0.3, hspace=0.3)
ax1 = fig.add_subplot(1,1,1)
ax1.scatter(ts,xs)
ax1.set_ylabel('Posición')

ax2 = fig.add_subplot(2,1,2)
ax2.scatter(ts,vs)
ax2.set_ylabel('Velocidad')
ax2.set_xlabel('Tiempo')
dateTime = datetime.now()
fig.savefig('files/grafico-' + dateTime.strftime("%Y-%m-%d_%H-%M-%S") + '.png', bbox_inches='tight')
