import cv2
import numpy as np

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('baby_yoda.mp4')

# framerate
fps = 25

# Check if video opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")


# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # size
        height, width, channels = frame.shape

        # 1. ORIGINAL 
        # Display the original frame
        cv2.imshow('Original', frame)
    
        # 2. GRAYSCALE
        # Conversion of BGR to grayscale 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the grayscale frame
        cv2.imshow('Gray', gray)

        # 3. BINARY IMAGE
        # adaptive thresholding to use different threshold values on different regions of the frame.
        binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                            cv2.THRESH_BINARY_INV, 11, 2)
        # Display the binary frame
        cv2.imshow('Binary', binary)

        # 4. DIFFERENT COLORS 
        frame[:,:int(width/3),0] = 255
        frame[:,int(width/3):int(2*width/3),1] = 255
        frame[:,int(2*width/3):int(width),2] = 255
        cv2.imshow('DiferentColors', frame)    


        # Press 'q' on keyboard to  exit
        if cv2.waitKey(fps) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break


# When everything done, release the video capture object
cap.release()
# Closes all the frames
cv2.destroyAllWindows()