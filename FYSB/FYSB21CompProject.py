import numpy as np

import matplotlib.pyplot as plt
from matplotlib import animation
from scipy import special



alpha = 1
ylim = 0.5
def u(x,t):
    return 0.5*((special.erf((ylim - x)/(np.sqrt(4*t*alpha)))) - (special.erf((-ylim - x)/(np.sqrt(4*t*alpha)))))





fig = plt.figure()
ax = plt.axes(xlim=[-10, 10], ylim=[0, 1.2])
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,


def animate(i):
    X = np.linspace(-3,3,10000)
    t = 0.1*i
    y = u(X,t)

    line.set_data(X,y)
    return line, 

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=300, interval=1000, save_count = 50, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
anim.save('basic_animation2.gif',writer = 'ffmpeg', fps=3)

plt.show()0i