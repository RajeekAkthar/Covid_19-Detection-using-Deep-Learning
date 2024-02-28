import os
import cv2
import time
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from django.shortcuts import render
from keras.models import load_model
from keras.preprocessing import image
from django.core.files.storage import FileSystemStorage

#Create your views here.
target_classes = ['covid', 'noncovid', 'normal']
IMAGE_SIZE = 256
model_file = 'C:/Users/rajee/Covid-WebApp/cov_cnn_web/predictor/model_weights/detect.h5'

def read_image(filepath):
    return cv2.imread(filepath)

def resize_image(image, image_size):
    return cv2.resize(image.copy(), image_size, interpolation=cv2.INTER_AREA)

def clear_mediadir():
    media_dir = "./media"
    for f in os.listdir(media_dir):
       os.remove(os.path.join(media_dir, f))

def index(request):
    if request.method == "POST":
        clear_mediadir()
        img = request.FILES['ImgFile']
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        img_path = fs.path(filename)

        pred_arr = np.zeros((1, IMAGE_SIZE, IMAGE_SIZE, 3))

        im = read_image(img_path)
        if im is not None:
            pred_arr[0] = resize_image(im, (IMAGE_SIZE, IMAGE_SIZE))

        pred_arr = pred_arr / 255

        model = load_model(model_file)
        label = model.predict(pred_arr)
        idx = np.argmax(label[0])
        cf_score = np.amax(label[0])

        prediction = "unknown" # initialize the variable to a default value

        if target_classes[idx] == 'covid':
            covid_model_file = 'C:/Users/rajee/Covid-WebApp/cov_cnn_web/predictor/model_weights/detect.h5'
            covid_model = load_model(covid_model_file)
            covid_label = covid_model.predict(pred_arr)
            covid_idx = np.argmax(covid_label[0])
            covid_cf_score = np.amax(covid_label[0])
            if covid_idx == 0:
                prediction = 'covid'
            else:
                prediction = 'noncovid'
            confidence_score = covid_cf_score
        elif target_classes[idx] == 'noncovid':
            prediction = 'noncovid'
            confidence_score = cf_score
        else:
            prediction = 'normal'
            confidence_score = cf_score
            
        print('Prediction: ', prediction)
        print('Confidence Score: ', confidence_score)
        
        response = {}
        response['row1'] = "Confidence Score--" + str(confidence_score)
        response['row2'] = "Prediction--" + str(prediction)
        response['image'] = "../media/" + img.name
        return render(request, 'index.html', response)
    else:
        return render(request, 'index.html')
