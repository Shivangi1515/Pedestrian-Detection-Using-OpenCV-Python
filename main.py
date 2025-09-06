#Pedestrian Detection using OpenCV-Python
import cv2 as cv
import imutils  #convenience library that simplifies basic image processing operations 

#HOG is Histogram of Oriented Gradient-->it is basically a feature detector that looks at image gradient and edges 
hog=cv.HOGDescriptor() #inbuild method of opencv library used for detecting people,used for detecting shapes like human

hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())  #used pretrained model to detect the pedestrian

# SVM is pretrained Support Vector Machine Classifier that recognises people based on HOG Features

cap=cv.VideoCapture('people.mp4')

while cap.isOpened():
    ret,img=cap.read()
    if ret:
        img=imutils.resize(img,width=min(400,img.shape[1]))
        (regions,_)=hog.detectMultiScale(img,winStride=(4,4),padding=(4,4),scale=1.05) #padding will help detect the object at the edges and scale will help to detect the pedestrian at various sizes

        for(x,y,w,h) in regions: #x,y,w,h are the coordinates of the rectangle
            cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        cv.imshow('img',img)

        if cv.waitKey(30) & 0xFF==ord('q'):
            break

    else :
            break

cap.release()
cv.destroyAllWindows()



