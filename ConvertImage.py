#converts image to a BGR png and a Greyscale 8-bit png
import cv2

simpleimage = cv2.imread('sample.jpg')
cv2.imwrite('simpleimage.png',simpleimage)

greyscaleimg = cv2.imread('sample.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('greyscaleimg.png',greyscaleimg)