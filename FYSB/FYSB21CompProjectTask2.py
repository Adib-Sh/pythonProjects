
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



pcm = plt.pcolormesh(u(X,Y,0.00))
plt.colorbar()


#Animation
def step(i):
    if i >= len(X): return
    pcm.set_array(u(X,Y,i))
    plt.draw()


anim = animation.FuncAnimation(fig, step, interval=50)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
anim.save('basic_animation2.gif',writer = 'ffmpeg',fps=10)

fig.show()



'''




import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.animation as animation

def update_plot(frame_number, zarray, plot):
    plot[0].remove()
    plot[0] = ax.plot_surface(x, y, zarray[:,:,frame_number], cmap="magma")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

N = 14
nmax=20
x = np.linspace(-4,4,N+1)
x, y = np.meshgrid(x, x)
zarray = np.zeros((N+1, N+1, nmax))

sig = lambda t: 1.5+np.sin(t*2*np.pi/nmax)
c = lambda x,y,t : 1/np.sqrt(sig(t))*np.exp(-(x**2+y**2)/sig(t)**2)

for t in range(nmax):
    zarray[:,:,t] = c(x,y,t)

plot = [ax.plot_surface(x, y, zarray[:,:,0], color='0.75', rstride=1, cstride=1)]
ax.set_zlim(0,1.5)
animate = animation.FuncAnimation(fig, update_plot, nmax, fargs=(zarray, plot))
animate.save('mesh.gif',writer = 'ffmpeg',fps=10)
plt.show()
'''