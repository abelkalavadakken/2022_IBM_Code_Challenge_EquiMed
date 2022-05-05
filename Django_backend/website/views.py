from distutils.command.sdist import sdist
from django.http import HttpResponse
from django.shortcuts import render
from Django_backend.settings import BASE_DIR
from .forms import ImageForm
from .models import Image
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Create your views here.

#mish activation 
def mish(inputs):
    return inputs * tf.math.tanh(tf.math.softplus(inputs))

tf.keras.utils.get_custom_objects().update({'mish': mish})



model = load_model(os.path.join(BASE_DIR,'models/cataractclassifierV9.h5'))


def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'analyse.html')
    form = ImageForm()
    img = Image.objects.all()
    return render(request,'home.html')

def analyse(request):
    img = Image.objects.all()
    l = len(img)
    x = img[l-1]
    img_path = str(BASE_DIR)+ x.photo.url
    img = image.load_img(img_path, target_size=(128,128,3))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    prediction = prediction.argmax()
    if prediction == 0:
        return render(request,'result.html')
    else:
        return render(request,'noresult.html')

    return render(request,'analyse.html')
