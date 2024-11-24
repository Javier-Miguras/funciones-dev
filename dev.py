import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-tf', type=int,help="tiempo final (horas)")
parser.add_argument('-pos', type=float,help="posicion inicial del objeto (km)")
parser.add_argument('-acel', type=float,default=10,help="aceleracion del objeto")
parser.add_argument('-vel', type=float,help="velocidad inicial (km/h)")
args = parser.parse_args()

print(args.acel)

def get_position(x0,t,v0,a):
    x = x0 + v0 * t + 0.5 * a * t**2  # Corrección de la fórmula faltaba el 1/2 xD
    return x

def get_velocities(v0,a,t):
    v = v0 + a*t
    return v

dt = 0.1
t0 = 0
tf = args.tf

ts = np.arange(t0,tf,dt) # para poder usar float y obtener resultado más precisos

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

fig = plt.figure(figsize=(6,5),dpi=150)
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

ax1 = fig.add_subplot(2,1,1)
ax1.scatter(ts,xs)
ax1.set_ylabel('Distancia a la tierra (km)')
print(ax1)

ax2 = fig.add_subplot(2,1,2)
ax2.scatter(ts,vs)
ax2.set_ylabel('Velocidad (km/h)')
ax2.set_xlabel('Tiempo (horas)')

# Ajustar los ticks en el eje X para que vayan de 100 en 100
#ax2.xaxis.set_major_locator(MultipleLocator(100))  # Ticks de 100 en 100 seg

dateTime = datetime.now()
fig.savefig('files/grafico-' + dateTime.strftime("%Y-%m-%d_%H-%M-%S") + '.png', bbox_inches='tight')
