import numpy as np

import matplotlib.pyplot as plt
from matplotlib import animation
from scipy import special



alpha = 1
ylim = 0.5
def u(x,t):
    return 0.5*((special.erf((ylim - x)/(np.sqrt(4*t*alpha)))) - (special.erf((-ylim - x)/(np.sqrt(4*t*alpha)))))




#Plot setup
fig = plt.figure()
ax = plt.axes(xlim=[-3.5, 3.5], ylim=[0, 1.2])
plt.ylabel('u(x,t)')
plt.xlabel('x')
plt.title('solution of the heat equation in 1-D')
x = np.linspace(-4,4,10000)
y = [u(x,0) for x in x]
y1 = [u(x,0.05) for x in x]
y2 = [u(x,0.1) for x in x]
y3 = [u(x,0.2) for x in x]
ax.plot(x,y, label='t=0')
ax.plot(x,y1, label='t=0.05s')
ax.plot(x,y2, label='t=0.1s')
ax.plot(x,y3, label='t=0.2s')

text = ax.text(0, 0, '')
ax.legend()


line, = ax.plot([], [], lw=3, label='0s<t<1.5s')
#Animation
def init():
    line.set_data([], [])
    return line,


def animate(i):
    X = np.linspace(-3,3,10000)
    t = 0.01*i
    y = u(X,t)
    text.set_text("time: " + str(round(t,2))+'s')
    text.set_position((-3,1.1))
    line.set_data(X,y)
    return line, 

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=150, interval=800, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
anim.save('task1gif',writer = 'ffmpeg',fps=10)

fig.show()