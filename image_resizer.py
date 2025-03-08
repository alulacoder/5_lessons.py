import cv2

img = cv2.imread("open_cv/image/pikachu.jpeg",1)
cv2.imshow("Original Image", img)

# The order of dimensions is (WIDTH, HEIGHT)
resized = cv2.resize(img, (500, 250))
cv2.imshow("resizedImage", resized)

cv2.waitKey(0)
cv2.destroyAllWindows ()