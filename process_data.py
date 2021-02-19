import numpy as np
import matplotlib.pyplot as plt
import os as os
import cv2
import random
import pickle

DATADIR = "./PokemonDataSmall"
CATEGORIES = ['Charizard', "Bulbasaur", "Charmander"]
IMG_SIZE = 1000

training_data = []

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img))
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass
create_training_data()
print(len(training_data))

random.shuffle(training_data)

X = [] # feature set
y = [] # labels

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 3) # -1 means any number of features. 3 means colored, use 1 for grayscale

pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()
pickle_in = open("X.pickle", "rb")
X = pickle.load(pickle_in)
