import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON,OFF]

def randomGrid(N):
	"""Returns a grid of NxN random values."""
	return np.random.choice(vals,N*N, p=[0.2,0.8]).reshape(N,N)


def addGlider(i,j,grid):
	"""Adds a glider with top left cell at (i,j)"""
	glider = np.array([[OFF,OFF,ON],[ON,OFF,ON],[OFF,ON,ON]])
	grid[i:i+3,j:j+3] = glider
def update(frameNum, img, grid, N):
	# copy grid since e require 8 neighbors for calculation
	# and we go line by line
	newGrid = grid.copy()
	for i in range(N):
		for j in range(N):
			# compute 8-neighbor sum using torroidial boundary consitions
			# x and y wrap around so that the simulatoin
			# takes place on a toroidial surface
			total = int((grid[i,(j-1)%N]+grid[i,(j+1)%N]+
						grid[(i-1)%N,j]+grid[(i+1)%N,j]+
						grid[(i-1)%N,(j-1)%N]+grid[(i-1)%N,(j+1)%N]+
						grid[(i+1)%N,(j-1)%N]+grid[(i+1)%N,(j+1)%N])/255)

			if grid[i,j] == ON:
				if(total <2) or (total>3):
					newGrid[i,j] = OFF
			else:
				if total ==3:
					newGrid[i,j] = ON
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
	parser.add_argument('--glider', action='store_true', required=False)
	args = parser.parse_args()

	# set grid size
	N = 100
	if args.N and int(args.N) > 8:
		N = int(args.N)

	# set animation update value
	updateInterval = 50
	if args.interval:
		updateInterval = int(args.interval)

	#declare grid
	grid = np.array([])
	# check if glider flag is specified
	if args.glider:
		grid = np.zeros(N*N).reshape(N,N)
		addGlider(1,1,grid)
	else:
		grid = randomGrid(N)

	# setup animation
#	fig, ax = plt.subplots()
	fig = plt.figure()
	ax = fig.add_subplot(111)
	img = ax.imshow(grid,interpolation='nearest')
	ani = animation.FuncAnimation(fig,update,fargs=(img,grid,N,),
							frames=10,interval=updateInterval,save_count=50)										
	#number of frames?
	# set the ouput file
	if args.movfile:
		ani.save(args.movfile,fps=30,extra_args=['-vcodec','libx264'])

	plt.show()

# call main()
if __name__ == '__main__':
	main()
