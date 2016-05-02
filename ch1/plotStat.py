import plistlib
import numpy as np
import matplotlib.pyplot as plt

def plotStats(filename):
	#read in a playlist
	plist = plistlib.readPlist(filename)

	# get the tracks from the playlist
	tracks = plist['Tracks']

	# create lists of sing ratings and track duration
	ratings = []
	durations = []

	# iterate through the tracks
	for trackId, track in tracks.items():
		try:
			ratings.append(track['Album Rating'])
			durations.append(track['Total Time'])
		except:
			pass

	# ensure valid data is collected
	if ratings ==[] or durations == []:
		print(' No Album Rating/Total Time data in %.s' % filename)
		return

	# scatter plot
	x = np.array(durations, np.int32)
	#convert to minutes
	x = x/60000.0
	y = np.array(ratings,np.int32)

	plt.subplot(2,1,1)
	plt.plot(x,y,'o')
	plt.axis([0,1.05*np.max(x), -1, 110])
	plt.xlabel('Track duration')
	plt.ylabel('Track Rating')

	#plot histogram
	plt.subplot(2,1,2)
	plt.hist(x, bins=20)
	plt.xlabel('Track Duration')
	plt.ylabel('Count')

	plt.show()



