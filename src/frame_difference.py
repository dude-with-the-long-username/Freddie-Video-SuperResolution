import numpy as np
import cv2

# Capture video from file
cap=cv2.VideoCapture('../240p.mp4')

old_frame = None

while True:

    ret, frame = cap.read()

    if ret == True:

        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    #This will convert frames to grayscale
        color_frame = frame

        if old_frame is not None:
            diff_frame = color_frame - old_frame
            diff_frame -= diff_frame.min()
            disp_frame = np.uint8(255.0*diff_frame/float(diff_frame.max()))
            cv2.imshow('diff_frame',disp_frame)
        old_frame = color_frame

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    else:
        print('ERROR!')
        break

cap.release()
cv2.destroyAllWindows()