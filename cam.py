import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorKNN()
#fgbg = cv2.createBackgroundSubtractorMOG2()

#fgbg = cv2.createBackgroundSubtractorMOG2()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

	#make mirror image
    flipped = cv2.flip(frame,1)
	
    fgmask = fgbg.apply(flipped)
	
    # Display the resulting frame
    cv2.imshow('frame',fgmask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()