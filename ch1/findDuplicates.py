import plistlib

def findDuplicates(filename):
	print('finding duplicate tracks in %s ... ' % filename)

	# read the play list
	plist = plistlib.readPlist(filename)

	# get tracks form Track dictionary
	# track is a dictionary with 
	tracks = plist['Tracks']

	#create track name dictionary
	trackNames = {}

	# iterate through the tracks
	for trackId, track in tracks.items():
		try:
			name = track['Name']
			duration = track['Total Time']

			# look for existing entries
			if name in trackNames:
				# if a name and duration match, increment the count
				# round the track length to the nearest second
				if duration//1000 == trackNames[name][0]//1000:
					count = trackNames[name][1]
					trackNames[name] = (duratin, count+1)
			else:
				# add dictionary entry as tuple (duration, count)
				trackNames[name] = (duration, 1)
		except:
			#ignore
			pass
				
	# store duplicates
	dups = []
	for k, v in trackNames.items():
		if v[1] > 1:
			dups.append((v[1],k))
	# save duplicates to file
	if len(dups) > 0:
		print ("found %d duplicates. Track names saved to dup.txt" % len(dups))
	else:
		print ("No duplicates tracks found.")

	f = open("dups.txt", 'w')
	for val in dups:
		f.write("[%d] %s\n" % (val[0],val[1]))
	f.close()


