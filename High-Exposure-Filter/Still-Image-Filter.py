# Opencv Still Image Test Program
# Mission is to print black only from the primary light sources in the photo

import cv2
import numpy as np


# Read image from file as grayscale
img = cv2.imread('test.jpg',cv2.IMREAD_GRAYSCALE)

# Throw away return value in underscore
# threshold(source_image, threshold_val, transformed_val, threshold_type)
_, thresh = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)

# declare kernel used for erosion and dilation
kernel = np.ones((5,5), np.uint8)

# erode away small areas in thresholded image
eroded = cv2.erode(thresh, kernel, iterations=10)

# dilate (expand) remaining white areas
dilated = cv2.dilate(eroded, kernel, iterations=40)
dilated = cv2.bitwise_not(dilated)

# getting shape of original image for resize
height, width = img.shape[:2]

# scales image by the inverse of resize_factor
resize_factor = 5

height //= resize_factor
width //= resize_factor

img = cv2.resize(img, (width, height))
eroded = cv2.resize(eroded, (width, height))
dilated = cv2.resize(dilated, (width, height))

# Displays images
cv2.imshow('Test Image', img)
# cv2.imshow("Eroded", eroded)
cv2.imshow("Dilated", dilated)

# Not yet functional program exit
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
