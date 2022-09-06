# USAGE
# python analyze_covers.py --output visualizations

# import the necessary packages
from __future__ import print_function
import numpy as np
import argparse
import argparse
import json
import os 
import cv2
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('--indir', type=str, required=True)
parser.add_argument('--outdir', type=str, required=True)
args = parser.parse_args()
indir = args.indir
outdir = args.outdir


# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-o", "--output", required=True,
# 	help="path to output visualizations directory")
# args = vars(ap.parse_args())

# # load the JSON data file
# data = json.loads(open("output.json").read())
covers = []


def average(file):
	cover = None
	if(".png" in file or ".jpg" in file or "jpeg" in file):
		cover = cv2.imread(indir+"/"+file)
	# if(file.split('.')[0].endswith('1')):
		# if the image is None, then there was an issue loading it
			# (this happens for ~3 images in the dataset, likely due to
			# a download problem during the scraping process)
	if cover is not None:
			# resize the magazine cover, flatten it into a single
			# list, and update the list of covers
		cover = cv2.resize(cover, (8840, 8840))
		covers.append(cover)


# for filename in os.listdir('/Users/aarati/Desktop/teddy'):
# 	average(filename)
import glob

for filename in os.listdir(indir + '/'):
    average(filename)

avg = np.average(covers, axis=0).reshape((8840, 8840, 4)).astype("uint8")
p = "{}/{}.png".format(outdir, 'averaged')
cv2.imwrite(p, avg)

# loop over each individual decade Time magazine has been published
# for decade in np.arange(1920, 2020, 10):
# 	# initialize the magazine covers list
# 	print("[INFO] processing years: {}-{}".format(decade, decade + 9))
# 	covers = []

# 	# loop over the magazine issues belonging to the current decade
# 	for row in filter_by_decade(decade, data):
# 		# load the image
# 		cover = cv2.imread("output/{}".format(row["files"][0]["path"]))

# 		# if the image is None, then there was an issue loading it
# 		# (this happens for ~3 images in the dataset, likely due to
# 		# a download problem during the scraping process)
# 		if cover is not None:
# 			# resize the magazine cover, flatten it into a single
# 			# list, and update the list of covers
# 			cover = cv2.resize(cover, (400, 527)).flatten()
# 			covers.append(cover)

	# compute the average image of the covers then write the average
	# image to disk
	# avg = np.average(covers, axis=0).reshape((527, 400, 3)).astype("uint8")
	# p = "{}/{}.png".format(args["output"], decade)
	# cv2.imwrite(p, avg)
