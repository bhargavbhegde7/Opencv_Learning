import cv2

videoRead = cv2.VideoCapture('sample_vid.mp4')
fps = videoRead.get(cv2.CAP_PROP_FPS)
size = (int(videoRead.get(cv2.CAP_PROP_FRAME_WIDTH)),
		int(videoRead.get(cv2.CAP_PROP_FRAME_HEIGHT)))

fourcc = cv2.cv.CV_FOURCC(*'X264')
videoWriter = cv2.VideoWriter('OutPutVid.avi',fourcc,fps,size)
success, frame = videoRead.read()
while success: #loop until there are no more frames.
	videoWriter.write(frame)
	success, frame = videoRead.read()
