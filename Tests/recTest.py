import cv2
import numpy as np
from keras.models import load_model
import unittest

from joblib import load


class Tests(unittest.TestCase):
    def test_face_recognition(self):
        names = []
        textfile = open("../names.txt", "r")
        for line in textfile:
            currentName = line[:-1]
            names.append(currentName)
        e = load_model("../facenet_keras.h5")
        model = load('../mlp.MODEL')
        photo = cv2.imread('../photo/val/rokas_p/1.jpg', 1)
        photo = cv2.resize(photo,(160,160))
        photo = photo.astype('float') / 255.0
        photo = np.expand_dims(photo, axis=0)
        photo = e.predict(photo)[0]
        photo = np.expand_dims(photo, axis=0)
        photo = model.predict(photo)[0]
        assert names[photo] == "rokas_p"
        self.assertTrue(names[photo] == "rokas_p")



if __name__ == "__main__":
    unittest.main()