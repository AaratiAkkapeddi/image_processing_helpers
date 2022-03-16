# import the necessary packages
#this is so confusing
from helpers.face_utils import FaceAlignerNoCrop
from helpers.face_utils import rect_to_bb
import argparse
import imutils
import dlib
import cv2
import os
import random

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor and the face aligner
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
fa = FaceAlignerNoCrop(predictor, desiredFaceWidth=2048)
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('--indir', type=str, required=True)
parser.add_argument('--outdir', type=str, required=True)
# Print "Hello" + the user input argument
# Parse the argument
args = parser.parse_args()
print('processing images from', args.indir)
print('saving images to', args.outdir)
folder = args.indir
outdir = args.outdir
if not os.path.isdir(outdir):
	os.mkdir(""+outdir)


def center_face (filename):
	print(filename)
	if ".jpg" in filename or ".png" in filename or ".jpeg" in filename:
		# load the input image, resize it, and convert it to grayscale
		image = cv2.imread(folder+'/' + filename)
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
			cv2.imwrite(outdir + "/"+ str(random.randint(0,90)) + "_"+filename, faceAligned)
	
#iterate through folder of images
for filename in os.listdir(folder + '/'):
    center_face(filename)


