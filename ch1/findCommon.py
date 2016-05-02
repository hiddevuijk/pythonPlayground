import plistlib

def findCommonTracks(fileNames):
	# a list of sets of track names
	trackNameSets = []
	for fileName in fileNames:
		#create new set
		trackNames = set()

		# read in playlist
		plist = plistlib.readPlist(fileName)

		# get the tracks
		tracks = plist['Tracks']
		#iterate through the tracks
		for trackId, track in tracks.items():
			try:
				# add the track name to a set
				trackNames.add(track['Names'])
			except:
				pass
			# add to list
			trackNameSets.append(trackNames)

	#get the set of common tracks
	commonTracks = set.intersection(*trackNameSets)

	# write to file
	if len(commonTracks) > 0:
		f = open("common.txt", 'w')
		for val in commonTracks:
			s = "%s\n" % val
			f.write(s.encode("UTF-8"))
		f.close()
		print("%d common tracks found. "
			  "Track names written to common.txt." % len(comoonTracks))
	else:
		print( " No common tracks.")


