from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.applications.inception_v3 import InceptionV3

def load():

    model = models.load_model('C:\\python\\diplom\\my_model.h5')
    return model