import cv2
import numpy as np

# Read the image
image = cv2.imread('mask_11.png', 0)  # Read as grayscale

# Threshold the image to get a binary image
_, binary_image = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)

# Find contours in the binary image
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get the bounding box of the contour
x, y, w, h = cv2.boundingRect(contours[0])

# Draw the bounding box on the original image
result_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.rectangle(result_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the result
cv2.imshow('Result', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
