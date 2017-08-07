import cv2

clicked = False
def onMouse(event,x,y,flags,param):
	global clicked
	if event == cv2.EVENT_LBUTTONUP:
		clicked = True

camCaptur = cv2.VideoCapture('sample_vid.mp4')
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow',onMouse)

print ('Showing vid feed. Click window or press any key to stop.')
success, frame = camCaptur.read()
while success and cv2.waitKey(1) == -1 and not clicked:
	cv2.imshow('MyWindow',frame)
	success, frame = camCaptur.read()

cv2.destroyWindow('MyWindow')