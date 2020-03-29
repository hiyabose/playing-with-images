#to import the packages
import cv2
import numpy as np

#to read the image. P.S. always save yur image inside the python file
hand= cv2.imread('h1.png', 0)


#threshold....to highlight the image
ret, thresh = cv2.threshold(hand, 70,255, cv2.THRESH_BINARY)

contours, hiearchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


#to draw the line around the hand
hull =[cv2.convexHull(c) for c in contours]

final = cv2.drawContours(hand, hull, -1, (255,0,0))

blur = cv2.GaussianBlur(hand, (5,5), 0)

#to show the image
cv2.imshow('Original Image',hand)
cv2.imshow('Thresh', thresh)
cv2.imshow('Convex Hull', final)
cv2.imshow('blur',blur)

cv2.waitKey(0)
cv2.destroyAllWindows()

