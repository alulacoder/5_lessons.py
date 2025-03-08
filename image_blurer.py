import cv2

image = cv2.imread ("open_cv/image/pikachu.jpeg")

cv2. imshow('Original Image', image)
cv2.waitKey(0)

# Gaussian Blur - used mostly in machine learning preprocessing steps
Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2. imshow( 'Gaussian Blurring', Gaussian) 
cv2.waitKey(0)

# Median Blur - used in digital processing preserves edges but removes noise
median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median) 
cv2.waitKey(0)

# Bilateral Blur - only sharp edges are preserved here
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()