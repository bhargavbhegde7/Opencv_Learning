import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorKNN()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

	#make mirror image
    flipped = cv2.flip(frame,1)
	
    
    #fgmask = fgbg.apply(flipped)
	
    #blurred = cv2.GaussianBlur(flipped, (11, 11), 0)
	
	#eroded = cv2.erode(fgmask, None, iterations=2)
    dilated = cv2.dilate(fgmask, None, iterations=2)
	
	
    # Display the resulting frame
    cv2.imshow('frame',dilated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()