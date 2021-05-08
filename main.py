from DetectAllFaces import extract_face
import argparse
from keras.models import load_model
from CreateEnbeddings import get_embedding
from numpy import asarray
from sklearn.preprocessing import Normalizer
from joblib import load
from numpy import expand_dims
from numpy import max

mlp_model = None
facenet_model = None
name_list = ['edgar_k', 'edvinas_s', 'emilis_z', 'gediminas_a_k', 'jokubas_d_b', 'laimonas_j', 'marius_s', 'rokas_p']

def initialize_models(facenet_path, mlp_path, embeddings_path):
    print("Initializing models")
    global mlp_model, facenet_model
    facenet_model = load_model(facenet_path)
    mlp_model = load(mlp_path)
    print("Models Loaded")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--facenet", "-f", default = "facenet_keras.h5", help = "path to facenet model")
    parser.add_argument("--embeddings", "-e", default="photo-embeddings.npz", help = "enbedded pictures")
    parser.add_argument("--mlp", "-s", default="mlp.MODEL", help = "mlp trained file")
    parser.add_argument("--image", "-i", default="photo/val/laimonas_j/5.jpg", help = "image to detect")

    args = parser.parse_args()
    initialize_models(args.facenet, args.mlp, args.embeddings)



    # print(args.image)
    detectedFace = extract_face(args.image)
    embeddings = expand_dims(asarray(get_embedding(facenet_model, detectedFace)),axis=0)
    in_encoder = Normalizer(norm='l2')
    embeddings = in_encoder.transform(embeddings)
    prob = mlp_model.predict_proba(embeddings)
    confidence = max(prob)
    p_class = mlp_model.predict(embeddings)[0]
    print(prob)
    print(confidence*100)
    print(name_list[p_class])





