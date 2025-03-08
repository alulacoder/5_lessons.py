import cv2

image1 = cv2.imread('open_cv/image/input1.png')
image2 = cv2.imread('open_cv/image/input2.png')
weightedSum = cv2.addWeighted (image1, 0.5, image2, 0.4, 1.5)
sub = cv2.subtract(weightedSum, image2)

cv2.imshow('3 dot Image', weightedSum)
cv2.imshow('2 dot Image', image2)
cv2.imshow('Subtracted Image', sub)

cv2.waitKey(0)
cv2.destroyAllWindows()