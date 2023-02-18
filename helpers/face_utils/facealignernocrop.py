# import the necessary packages
from .helpers import FACIAL_LANDMARKS_68_IDXS
from .helpers import FACIAL_LANDMARKS_5_IDXS
from .helpers import shape_to_np
import numpy as np
import cv2

class FaceAlignerNoCrop:
	def __init__(self, predictor, desiredLeftEye=(0.35, 0.35),
		desiredFaceWidth=1030, desiredFaceHeight=None):
		# store the facial landmark predictor, desired output left
		# eye position, and desired output face width + height
		self.predictor = predictor
		self.desiredLeftEye = desiredLeftEye
		self.desiredFaceWidth = desiredFaceWidth
		self.desiredFaceHeight = desiredFaceHeight

		# if the desired face height is None, set it to be the
		# desired face width (normal behavior)
		if self.desiredFaceHeight is None:
			self.desiredFaceHeight = self.desiredFaceWidth

	def align(self, image, gray, rect):
		# convert the landmark (x, y)-coordinates to a NumPy array
		shape = self.predictor(gray, rect)
		shape = shape_to_np(shape)

		
		#simple hack ;)
		if (len(shape)==68):
			# extract the left and right eye (x, y)-coordinates
			(lStart, lEnd) = FACIAL_LANDMARKS_68_IDXS["left_eye"]
			(rStart, rEnd) = FACIAL_LANDMARKS_68_IDXS["right_eye"]
		else:
			(lStart, lEnd) = FACIAL_LANDMARKS_5_IDXS["left_eye"]
			(rStart, rEnd) = FACIAL_LANDMARKS_5_IDXS["right_eye"]
			
		leftEyePts = shape[lStart:lEnd]
		rightEyePts = shape[rStart:rEnd]

		# compute the center of mass for each eye
		leftEyeCenter = leftEyePts.mean(axis=0).astype("int")
		rightEyeCenter = rightEyePts.mean(axis=0).astype("int")

		# compute the angle between the eye centroids
		dY = rightEyeCenter[1] - leftEyeCenter[1]
		dX = rightEyeCenter[0] - leftEyeCenter[0]
		angle = np.degrees(np.arctan2(dY, dX)) - 180

		# compute the desired right eye x-coordinate based on the
		# desired x-coordinate of the left eye
		desiredRightEyeX = 1.0 - self.desiredLeftEye[0]

		# determine the scale of the new resulting image by taking
		# the ratio of the distance between eyes in the *current*
		# image to the ratio of distance between eyes in the
		# *desired* image
		dist = np.sqrt((dX ** 2) + (dY ** 2))
		desiredDist = (desiredRightEyeX - self.desiredLeftEye[0])
		desiredDist *= self.desiredFaceWidth
		# scale = 200 / dist *
		scale = 150 / dist

		# compute center (x, y)-coordinates (i.e., the median point)
		# between the two eyes in the input image
		eyesCenter = (int((leftEyeCenter[0] + rightEyeCenter[0]) // 2),
			int((leftEyeCenter[1] + rightEyeCenter[1]) // 2))

		# grab the rotation matrix for rotating and scaling the face
		angle = 0
		M = cv2.getRotationMatrix2D(eyesCenter, angle, scale)

		# update the translation component of the matrix
		tX = 1024 #512
		tY = 768
		M[0, 2] += (tX - eyesCenter[0])
		M[1, 2] += (tY - eyesCenter[1]) 
		# apply the affine transformation
		# (w, h) = (self.desiredFaceWidth, self.desiredFaceHeight)
		(w, h) = (2048, 1536)
		# (w, h) = (8840, 8840)
		output = cv2.warpAffine(image, M, (w,h),
			flags=cv2.INTER_CUBIC,borderMode=cv2.BORDER_CONSTANT,
                           borderValue=(0,0,0,0))

		# return the aligned face
		tmp = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
		# Applying thresholding technique
		_, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
		# Using cv2.split() to split channels 
		# of coloured image
		b, g, r = cv2.split(output)
		# Making list of Red, Green, Blue
		# Channels and alpha
		rgba = [b, g, r, alpha]
		# Using cv2.merge() to merge rgba
		# into a coloured/multi-channeled image
		dst = cv2.merge(rgba, 4)
		return dst
