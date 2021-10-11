# import the necessary packages
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
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
fa = FaceAligner(predictor, desiredFaceWidth=2048)

def center_face (filename):
	print(filename)
	if ".jpg" in filename:
		# load the input image, resize it, and convert it to grayscale
		image = cv2.imread('./mom_augmented/' + filename)
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
			cv2.imwrite("./output_mom2/"+ str(random.randint(0,90)) + "_"+filename, faceAligned)
		
#iterate through folder of images
for filename in os.listdir('./mom_augmented/'):
    center_face(filename)
