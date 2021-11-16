import sys
import os
import argparse
import cv2

parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('--video', type=str, required=True)
parser.add_argument('--outdir', type=str, required=True)
# Print "Hello" + the user input argument
# Parse the argument
args = parser.parse_args()
print('processing images from', args.video)
print('saving images to', args.outdir)
video = args.video
outdir = args.outdir
if not os.path.isdir(outdir):
	os.mkdir(""+outdir)

vidcap = cv2.VideoCapture(video)
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  if count % 1 == 0:
	  print ('Read a new frame: ', success)
	  if success:
	  	cv2.imwrite(outdir+'/' + "frame%d.jpg" % count, image)     # save frame as JPEG file
  count += 1	  