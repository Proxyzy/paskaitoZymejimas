import cv2
import numpy as np
from getNames import getStudentNames
from DetectFace import face
from embedding import emb
from joblib import load
from retreive_pymongo_data import database



def rec():
    fd = face()
    e = emb()
    model=load('mlp.MODEL')
    data=database()
    a = []
    name_list = getStudentNames()
    for name in name_list:
        a.append(0)
    print(a)
    name = None

    print('attendance till now is ')
    data.view()

    cap=cv2.VideoCapture(0)
    ret=True
    while ret:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        det, coor = fd.detectFace(frame)
        if (det is not None):
            for i in range(len(det)):
                detected = det[i]
                k = coor[i]
                f = detected
                detected = cv2.resize(detected, (160, 160))
                detected = detected.astype('float') / 255.0
                detected = np.expand_dims(detected, axis=0)
                feed = e.calculate(detected)
                feed = np.expand_dims(feed, axis=0)
                prob = model.predict_proba(feed)
                prediction = model.predict(feed)[0]
                result = int(np.argmax(prediction))
                if (np.max(prob) > .80):
                    label = name_list[prediction]
                    print(label)
                    print(prob)
                    if(a[prediction]==0):

                        data.update(label)
                    a[prediction] = 1
                    # print(a)
                else:
                    label = 'unknown'

                cv2.putText(frame, label, (k[0], k[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                cv2.rectangle(frame, (k[0], k[1]), (k[0] + k[2], k[1] + k[3]), (252, 160, 39), 3)
                cv2.imshow('onlyFace', f)
        cv2.imshow('frame', frame)
        if (cv2.waitKey(1) & 0XFF == ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()
    data.export_csv()

if __name__ == "__main__":
    rec()