import cv2
import imutils
import math
import numpy as np

hsvLower = (17, 168, 112)
hsvUpper = (255, 255, 255)

def getResizeBlurHsv(image):
	image = imutils.resize(image, width=600)
	blurred = cv2.GaussianBlur(image, (11, 11), 0)
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	return hsv

def getMasked(hsv):
	mask = cv2.inRange(hsv, hsvLower, hsvUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	return mask

def getCenter(image):

	hsv = getResizeBlurHsv(image)
	masked = getMasked(hsv)

	cnts = cv2.findContours(masked.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None
	if len(cnts) > 0:
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
	return center

img1 = cv2.imread("dist_cloth_1.png")
img2 = cv2.imread("dist_cloth_2.png")

center1 = getCenter(img1)
center2 = getCenter(img2)

print center1
print center2

distance = math.hypot(center2[0] - center1[0], center2[1] - center1[1])
print distance

#blank_image = np.zeros((1000,3000,3), np.uint8)

#newImg = imutils.resize(img1, width=600)
#cv2.line(newImg, center1, center2, (0,0,255), 1)

#------- to display ------
#cv2.imshow('image',newImg)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
