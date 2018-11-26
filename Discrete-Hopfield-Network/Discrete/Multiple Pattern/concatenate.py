import cv2
import numpy as np


# Open the input video files or camera stream.
capture1 = cv2.VideoCapture("ApproxNet.mp4")
i = 0
arr = "000000"

capture2 = cv2.imread('../ILSVRC2015/Airplane01/{}.JPEG'.format(arr[:-len(str(i))] + str(i)), cv2.IMREAD_UNCHANGED)

combinedSize = (capture2.shape[0]*2, capture2.shape[1])
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4',fourcc, 30.0, combinedSize)

# CvVideoWriter* videoWriter = cvCreateVideoWriter(outputFilename, CV_FOURCC('D','I','V','3'), FPS, combinedSize, TRUE);
# IplImage *frameOut = cvCreateImage(combinedSize, 8, 3);		// Create an empty RGB image for storing the combined frame.
# IplImage *frame1, *frame2;

# Process both video streams while atleast one is still running (AVI or MPG file or camera stream).
# frame1 = (IplImage*)1;	// Enter the loop.
# frame2 = (IplImage*)1;	// Enter the loop.
# while (frame1 || frame2) {
# 	// Get the next video frames.
# 	frame1 = cvQueryFrame( capture1 );
# 	frame2 = cvQueryFrame( capture2 );
# 	if (frame1 || frame2) {
# 		// Combine the 2 image frames into 1 big frame.	
# 		frameOut = combineImages(frame1, frame2);
# 		// Store the combined video frame into the new video file.
# 		cvWriteFrame(videoWriter, frameOut);
# 	}

while(capture1.isOpened()):
	ret, frame = cap.read()
    if ret==True:
        combined = np.column_stack((capture2, frame))

        out.write(combined)

        cv2.imshow('frame',combined)

        i = i+1
		capture2 = cv2.imread('../ILSVRC2015/Airplane01/{}.JPEG'.format(arr[:-len(str(i))] + str(i)), cv2.IMREAD_UNCHANGED)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break