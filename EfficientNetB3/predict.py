import numpy as np
from keras.src.saving import load_model
import os
from keras.src.utils import load_img, img_to_array
from requests import get


def preprocess_image(image_path, target_size=(256, 256)):
    img = load_img(image_path, target_size=target_size)
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    return x


def predict_image(image_data):
    model_path = 'C:/Users/Admin/Downloads/flaskapp/EfficientNetB3/efficientnet_XLA.h5'
    model = load_model(model_path, compile=False)
    prediction = model.predict(image_data)
    print(prediction)
    predicted_class = np.argmax(prediction)
    return predicted_class
