import re, argparse
import sys

from findDuplicates import *
from findCommon import *
from plotStat import *


def main():
	#create parser
	descStr = """
	This program analyzes playlist files (.xml) exported from itunes.
	"""

	parser = argparse.ArgumentParser(description = descStr)

	# add mutually exclusive group arguments
	group = parser.add_mutually_exclusive_group()

	# add excpected arguments
	group.add_argument('--common', nargs='*', dest='plFiles', required=False)
	group.add_argument('--stats', dest='plFile', required=False)
	group.add_argument('--dup', dest='plFileD', required=False)

	# parse args
	args = parser.parse_args()

	if args.plFiles:
		findCommonTracks(args.plFiles)
	elif args.plFile:
		plotStats(args.plFile)
	elif args.plFileD:
		findDuplicates(args.plFileD)
	else:
		print("these are not the tracks you are looking for.")

# main method
if __name__ == '__main__':
	main()

