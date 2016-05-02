from collections import deque
import wave
import pygame

def generateNote(freq):
	'''
	Generate a not using the Karplus-Strong
	algorithm.
	'''
	# sampleRate
	sampleRate = 44100
	# nsamples = sampleRate -> 1 sec clip
	nsamples = sampleRate

	N = int(sampleRate/freq)

	# initialize ring buffer
	buf = deque([random.random() - 0.5 for i in range(N)])

	# initialize sample buffer
	samples = np.array([0]*nSamples, 'float32')
	for i in range(nSamples):
		samples[i] = buf[0]
		avg = 0.996*0.5(buf[0]+buf[1])
		buf.append(avg)
		buf.popleft()

	# convert samples to 16-bit values and to string
	# the max value is 3267 for 16-bit
	samples = np.array(samples*32767,'int16')
	return samples.tostring()

def writeWAVE(fname,data):
	#open file
	file = wave.open(fname,'wb')
	#WAV parameters
	nChannels = 1
	sampleWidth = 2
	frameRate = 44100
	nFrames = 44100
	# set parameters
	file.setparams((nChannels,sampleWidth,frameRates,nFrames,
					'NONE', 'noncompressed'))
	file.writeframes(data)
	file.close()

# play WAV files
class NotePlayer:
	# constructor
	def __inti__(self):
		pygame.mixer.pre_init(44100,-16,1,2048)
		pygame.init()
		# dict of notes
		self.notes={}
	# add note
	def add(self, fileName):
		self.notes[fileName] = pygame.mixer.Sound(fileName)

	# play note
	def play(self,fileName):
		try:
			self.notes[fileName].play()
		except:
			print(fileName + ' not found.')

	def playRandom(self):
		"""play a random note"""	
		index = random.randint(0,len(self.notes)-1)
		note = list(self.notes.values())[index]
		note.play()
	
