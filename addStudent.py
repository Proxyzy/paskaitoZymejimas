import cv2
import numpy as np
from retreive_pymongo_data import database
import os

def createStudent(name):
    pic_no=0
    data = database()
    data.addStudent(name)
    os.makedirs("photo/train/"+name)
    fa=cv2.CascadeClassifier('haarcascades/faces.xml')
    cap=cv2.VideoCapture(0)
    ret=True
    while ret:
        ret,frame=cap.read()
        frame=cv2.flip(frame,1)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=fa.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cropped=frame[y:y+h,x:x+w]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2,cv2.LINE_AA)
            pic_no=pic_no+1
            cv2.imwrite("photo/train/"+name+'/'+str(pic_no)+'.jpg',cropped)
        cv2.imshow('frame',frame)
        cv2.waitKey(100)
        if(pic_no>50):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    createStudent()