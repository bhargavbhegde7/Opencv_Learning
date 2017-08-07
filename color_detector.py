# import the necessary packages
import numpy as np
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
# load the image
image = cv2.imread(args["image"])

#image = cv2.imread('RGB.jpg')
image = cv2.imread('green_tape_2.jpeg')

# define the list of boundaries
boundaries = [
	([17, 15, 100], [50, 56, 200]),#red
	([86, 31, 4], [220, 88, 50]),#blue
	([25, 146, 190], [62, 174, 250]),#--
	([103, 86, 65], [145, 133, 128])#---
]

#supposed to be green, worked for adrian
'''
upper - 29, 86, 6
lower - 64, 255, 255
'''

# loop over the boundaries
'''
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
 
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)
	'''

'''
#yellow ball HSV
lower = np.array([0, 176, 114], dtype = "uint8")
upper = np.array([30, 255, 255], dtype = "uint8")	
'''

'''
#green tape HSV
lower = np.array([31, 61, 203], dtype = "uint8")
upper = np.array([42, 173, 255], dtype = "uint8")
'''

#green tape 2
lower = np.array([40, 58, 122], dtype = "uint8")
upper = np.array([112, 210, 203], dtype = "uint8")

'''
#green tape RGB
lower = np.array([82, 220, 145], dtype = "uint8")
upper = np.array([217, 255, 255], dtype = "uint8")
'''

#rubik's cube image
'''
lower = np.array([86, 31, 4], dtype = "uint8")
upper = np.array([220, 88, 50], dtype = "uint8")
'''

# find the colors within the specified boundaries and apply
# the mask
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower, upper)
output = cv2.bitwise_and(image, image, mask = mask)

# show the images
#cv2.imshow("images", np.hstack([image, output]))
cv2.imshow("images", mask)
#cv2.imshow("images", output)
cv2.waitKey(0)