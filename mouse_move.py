# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import pyautogui
 
# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
'''
#green ball of example
greenLower = (29, 86, 6)#bgr
greenUpper = (64, 255, 255)#bgr
'''

'''
#for the yellow ball video
greenLower = (17, 168, 112)
greenUpper = (255, 255, 255)
'''

#red rubix cube, cloth video
greenLower = (17, 168, 112)
greenUpper = (255, 255, 255)


pts = deque()

camera = cv2.VideoCapture('track_red.mp4')
path = []
count = 0
color = (0, 0, 255)
# keep looping
circle_img = cv2.imread("circle.png", -1)
x_offset=y_offset=50
while True:
	count = count+1
	# grab the current frame
	(grabbed, frame) = camera.read()
 
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if not grabbed:
		break
 
	# resize the frame, blur it, and convert it to the HSV
	# color space
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None

	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		# only proceed if the radius meets a minimum size
		if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
			pyautogui.moveTo(center[0],center[1])
 
	# update the points queue
	#if count%10 == 0:
	'''
	if center in pts:
		print 'closed path found'.count
		'''

	'''
	if center in pts:
		print count
	'''
	'''
	if count%10==0:
		pts.appendleft(center)
	'''
	pts.appendleft(center)
	
	
	if center is not None and center[0] >= 384:
		#print center
		color = (0, 255, 0)
	else:
		color = (0, 0, 255)

	path.append(center)
	#print center

	# loop over the set of tracked points
	for i in xrange(1, len(pts)):
		# if either of the tracked points are None, ignore
		# them
		if pts[i - 1] is None or pts[i] is None:
			continue
 
		# otherwise, compute the thickness of the line and
		# draw the connecting lines
		#thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
		#cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
		'''
		if pts[i - 1] == pts[i] and count%10 == 0:
			print ' found '
		'''
		cv2.line(frame, pts[i - 1], pts[i], color, 1)
		cv2.rectangle(frame,(384,0),(510,128),color,3)
		#frame[y_offset:y_offset+circle_img.shape[0], x_offset:x_offset+circle_img.shape[1]] = circle_img
		
 
	# show the frame to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
# cleanup the camera and close any open windows
print "---------------------------------------------"
#print type(path)
print "---------------------------------------------"
camera.release()
cv2.destroyAllWindows()