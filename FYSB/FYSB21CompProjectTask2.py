import numpy as np

import matplotlib.pyplot as plt
from matplotlib import animation
from scipy import special

# mesh
x = np.linspace(0, 50, 100)
y = np.linspace(0, 50, 100)
X, Y = np.meshgrid(x, y)

# center point
r0 = [17.5, 37.5]

# Distance
R = np.sqrt((r0[0] - X) ** 2 + (r0[1] - Y) ** 2)

Rmax = 2.5
# Equation
alpha = 2
Rlim = 0.5
u0=100
def u(x,y,t):
    return u0*0.5*((special.erf((Rlim - R)/(np.sqrt(4*t*alpha)))) - (special.erf((-Rlim - R)/(np.sqrt(4*t*alpha)))))


# Ploting
fig = plt.figure()
Z = np.array(u(0,0,1)).reshape(len(y), len(x))
'''
plt.pcolormesh(X, Y, Z)
plt.colorbar()

plt.show()
'''
mesh, = plt.pcolormesh(X, Y, Z)
#Animation
def init():
    mesh.set_data(X,Y,Z)
    return mesh,


def animate(i):
    x = np.linspace(0, 50, 100)
    y = np.linspace(0, 50, 100)
    X, Y = np.meshgrid(x, y)
    t = 0.01*i
    y = u(X,Y,t)
    mesh.set_data(X,Y,Z)
    return mesh, 

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=150, interval=800, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
anim.save('basic_animation2.gif',writer = 'ffmpeg',fps=10)

fig.show()
