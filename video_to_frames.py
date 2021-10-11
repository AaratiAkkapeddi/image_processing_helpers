import sys
import argparse

import cv2

vidcap = cv2.VideoCapture("./mom_me.mp4")
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  if count % 1 == 0:
	  print ('Read a new frame: ', success)
	  if success:
	  	cv2.imwrite('./me_mom/' + "frame%d.jpg" % count, image)     # save frame as JPEG file
  count += 1	  