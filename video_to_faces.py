
# import the necessary packages
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
import argparse
import imutils
import dlib
import cv2
import os
import random
import sys
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
# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor and the face aligner
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
fa = FaceAligner(predictor, desiredFaceWidth=2048)

def center_face (image):
	image = imutils.resize(image, width=940)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# show the original input image and detect faces in the grayscale
	# image
	rects = detector(gray, 2)

	# loop over the face detections
	for rect in rects:
		# extract the ROI of the *original* face, then align the face
		# using facial landmarks
		
		faceAligned = fa.align(image, gray, rect)

		# display the output images
		cv2.imwrite(outdir+"/"+ str(random.randint(0,90)) + "_"+ "frame%d.jpg" % count, faceAligned)
		
vidcap = cv2.VideoCapture(video)
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  if count % 10 == 0:
	  print ('Read a new frame: ', success)
	  if success:
	  	center_face(image)
	 
  count += 5	  
















