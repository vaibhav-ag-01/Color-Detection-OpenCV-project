import numpy as np
import cv2

video = cv2.VideoCapture('abc.mp4') # 0 for webcam

check,frame = video.read()
while check:
    #Reading Frame
    check,frame = video.read()
    #Resizing Frame
    resized_frame = cv2.resize(frame,(500,300))
    
    #Filtering the image
    filtered_img = cv2.cvtColor(resized_frame,cv2.COLOR_BGR2HSV)
    
    #Detecting Red Color

    low_red = np.array([161,155,84])
    high_red = np.array([179, 255, 255])

    red_mask = cv2.inRange(filtered_img,low_red,high_red)

    red = cv2.bitwise_and(resized_frame,resized_frame,mask = red_mask)

    #Detection Blue Color

    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])

    blue_mask = cv2.inRange(filtered_img,low_blue,high_blue)
    blue = cv2.bitwise_and(resized_frame,resized_frame,mask = blue_mask)

    #Detection Green Color

    low_green = np.array([25, 55, 72])
    high_green = np.array([105, 255, 255])

    green_mask = cv2.inRange(filtered_img,low_green,high_green)
    green = cv2.bitwise_and(resized_frame,resized_frame,mask = green_mask)
    
    cv2.imshow('Frame',resized_frame) 
    cv2.imshow('Red',red)
    cv2.imshow('Blue',blue)
    cv2.imshow('Green',green)
    
    key = cv2.waitKey(15)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break
cv2.destroyAllWindows()   
