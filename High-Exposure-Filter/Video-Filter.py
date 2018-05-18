# Opencv Still Image Test Program
# Mission is to print black only from the primary light sources in the photo

import cv2
import numpy as np



# Read image from file as grayscale
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    if(ret != True):
        print("Video Capture inaccessible")
        break
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Throw away return value in underscore
    # threshold(source_image, threshold_val, transformed_val, threshold_type)
    _, thresh = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)

    # declare kernel used for erosion and dilation
    kernel = np.ones((5,5), np.uint8)

    # erode away small areas in thresholded image
    eroded = cv2.erode(thresh, kernel, iterations=10)

    # dilate (expand) remaining white areas
    dilated = cv2.dilate(eroded, kernel, iterations=10)
    dilated = cv2.bitwise_not(dilated)
    dilated = cv2.blur(dilated, (50,50))

    # getting shape of original image for resize
    height, width = img.shape[:2]

    # scales image by the inverse of resize_factor
    resize_factor = 2

    height = (int)(height / resize_factor)
    width = (int)(width / resize_factor)

    img = cv2.resize(img, (width, height))
    eroded = cv2.resize(eroded, (width, height))
    dilated = cv2.resize(dilated, (width, height))

    # Displays images
    cv2.imshow('Test Image', img)
    # cv2.imshow("Eroded", eroded)
    cv2.imshow("Dilated", dilated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
