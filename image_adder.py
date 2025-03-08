import cv2
import numpy as np

image1 = cv2.imread('open_cv/image/input1.png')
image2 = cv2.imread('open_cv/image/input2.png')

# 0.5 and 0.4 are weights to be multiplied for each pixel, @ is gamma_value (measurement of light)
weightedSum = cv2.addWeighted (image1, 0.5, image2, 0.4, 1.5)
weightedSum1 = cv2.addWeighted (image1, 0.5, image2, 0.4, 0)
cv2.imshow('Weighted Image bright', weightedSum) 
cv2.imshow('Weighted Image dull', weightedSum1) 
cv2.waitKey(0)
cv2.destroyAllWindows ()