import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = plt.axes(xlim=(0,2), ylim=(-2,2))
line,  = ax.plot([],[], lw=2)

def init():
	line.set_data([],[])
	return line

def animate(i):
	x = np.linspace(0,2,1000)
	y = np.sin(2*np.pi*(x-0.01*i))
	line.set_data(x,y)
	return line

anim = animation.FuncAnimation(fig,animate,init_func=init, frames=100, interval=20)
#anim.save('sin.mp4',fps=30,extra_args=['-vcodec', 'libx264'])
plt.show()

