import numpy as np

"inndata"
m = 0.5
g = 9.81
k = 50.0

"Startverdier"
t = 0
a = -g
v = 0
x = 0

"Tidssteg"
t_slutt = 10
dt = 0.01

"Lister for tid og utslag"
t_verdier = [t]
x_verdier = [x]

while t < t_slutt:
    v = v + a*dt
    x = x + v*dt
    t = t + dt
    a = -g-(k*x/m)
    
    t_verdier.append(t)
    x_verdier.append(x)
    
plot(t_verdier, x_verdier)
title('Fjærpendel')
xlabel ('tid(s)')
ylabel('Utlag(m)')
show()