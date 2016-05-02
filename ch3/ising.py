import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 1
OFF = -1
vals = [ON,OFF]

def randomGrid(N):
	"""Returns a grid of NxN random values."""
	return np.random.choice(vals,N*N, p=[0.2,0.8]).reshape(N,N)



def update(frameNum, img, grid, N,J,h,T):
	# copy grid since e require 8 neighbors for calculation
	# and we go line by line
	newGrid = grid.copy()
	for i in range(N):
		for j in range(N):
			# compute 8-neighbor sum using torroidial boundary consitions
			# x and y wrap around so that the simulatoin
			# takes place on a toroidial surface
			E = int(grid[i,(j-1)%N]+grid[i,(j+1)%N]+
						grid[(i-1)%N,j]+grid[(i+1)%N,j]+
						grid[(i-1)%N,(j-1)%N]+grid[(i-1)%N,(j+1)%N]+
						grid[(i+1)%N,(j-1)%N]+grid[(i+1)%N,(j+1)%N])


			E = grid[i,j]*(J*E+h)

			
			if E> 0:
				newGrid[i,j] = 1
			else:
				newGrid[i,j] = -1

	# update data
	img.set_data(newGrid)
	grid[:] = newGrid[:]
	return img

# main() function
def main():
	# parse arguments
	parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
	
	# add arguments
	parser.add_argument('--grid-size', dest='N', required=False)
	parser.add_argument('--mov-file', dest='movfile', required=False)
	parser.add_argument('--interval', dest='interval', required=False)
	parser.add_argument('--J', dest='J', required=False)
	parser.add_argument('--T',dest='T',required=False)
	parser.add_argument('--h',dest='h',required=False)

	args = parser.parse_args()

	# set grid size
	N = 10
	if args.N and int(args.N) > 8:
		N = int(args.N)

	# set animation update value
	updateInterval = 50
	if args.interval:
		updateInterval = int(args.interval)

	#declare grid
	grid = np.array([])
	grid = randomGrid(N)


	J = 1.
	if args.J:
		J = args.J

	T = 0.
	if args.T:
		T = args.T

	h = 0.
	if args.h:
		h = args.h

	# setup animation
	fig = plt.figure()
	ax = fig.add_subplot(111)
	img = ax.imshow(grid,interpolation='nearest',cmap='Greys')
	ani = animation.FuncAnimation(fig,update,fargs=(img,grid,N,J,h,T,),
							frames=10,interval=updateInterval,save_count=50)										
	#number of frames?
	# set the ouput file
	if args.movfile:
		ani.save(args.movfile,fps=30,extra_args=['-vcodec','libx264'])

	plt.show()

# call main()
if __name__ == '__main__':
	main()
