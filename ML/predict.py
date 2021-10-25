from tensorflow.keras.models import *
from CaptchaSequence import *
import matplotlib.image as mpimg
import numpy as np
import string

characters = string.digits + string.ascii_lowercase

coder = Coder(characters)
model = load_model('captcha_cnn_dilation.h5')
x = np.array([mpimg.imread('image2/cpb3.jpg') / 255])
y = model.predict(x)
print(''.join([coder.decode(item) for item in y]))