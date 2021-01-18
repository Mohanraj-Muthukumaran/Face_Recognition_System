import cv2

cap = cv2.VideoCapture(0) #using the default webcam of our system to capture video

#let use haarcascade classifier which is used to detect the face from other things

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
    ret, frame = cap.read() # capture the frame and return values from the video capture
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # converting the frame into gray frame

    if ret == False:
        continue

    # faces is the list of four values = [x,y,w,h] where x and y are the 'starting co-ordinates' and w, h are 'width and height' from which we can form four co-ordinates.
    faces = face_cascade.detectMultiScale(gray_frame,1.3,5)
    print(faces) # just printing the co-ordinates that we got from the classifier
    
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3) # indicating a rectange of blue(255,0,0) color around face by the co-ordinates that we got from the classifier
    
    cv2.imshow('Video Frame', frame)


    # Code for Closing the App
    key_pressed = cv2.waitKey(1) & 0xFF
    
    if key_pressed == ord('q'): # when 'q' key is pressed loop will get breaked ans close all windows
        break

cap.release()
cv2.destroyAllWindows()
