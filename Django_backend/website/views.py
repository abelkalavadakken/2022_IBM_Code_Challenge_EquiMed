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
def mish(inputs):
    return inputs * tf.math.tanh(tf.math.softplus(inputs))
tf.keras.utils.get_custom_objects().update({'mish': mish})

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
    new_model = load_model(os.path.join(BASE_DIR, 'models/cataractclassifierV10.h5'))
    new_model.summary()
    image_folder = str(BASE_DIR) + x.photo.url.replace("/","\\")
    # test_image = image.load_img(os.path.join(image_folder),target_size=(150,150))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = new_model.predict(test_image)
    if result == 1:
        return render(request,'result.html')
    else :
        return render(request,'noresult.html')

    return render(request,'analyse.html')
