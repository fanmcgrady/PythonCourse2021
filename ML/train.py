from tensorflow.keras.models import *
from tensorflow.keras.layers import *
from tensorflow.keras.callbacks import EarlyStopping, CSVLogger, ModelCheckpoint
from tensorflow.keras.optimizers import *
from CaptchaSequence import *
import string

characters = string.digits + string.ascii_lowercase
print(characters)
width, height, n_len, n_class = 180, 60, 4, len(characters)

# 1、搭CNN网络，参考VGG网络
input_tensor = Input((height, width, 3))
x = input_tensor
for i, n_cnn in enumerate([(2, 2), (2, 2), (2, 3), (1, 5)]):
    for j in range(n_cnn[0]):
        x = Conv2D(32 * 2 ** min(i, 3),
                   kernel_size=3 - 2 * j,
                   padding='same',
                   kernel_initializer='he_uniform',
                   dilation_rate=(n_cnn[0], n_cnn[0]))(x)
        x = BatchNormalization()(x)
        x = Activation('relu')(x)
    x = MaxPool2D(n_cnn[1])(x)
x = Flatten()(x)
x = [Dense(n_class, activation='softmax', name='c%d' % (i + 1))(x) for i in range(n_len)]
model = Model(inputs=input_tensor, outputs=x)

# 2、配置模型
# print(model.summary())
# from tensorflow.keras.utils import plot_model
# plot_model(model, to_file='cnn_dilation.png', show_shapes=True)

model.compile(loss='categorical_crossentropy',
              optimizer=Adam(1e-3, amsgrad=True),
              metrics=['accuracy'])

# 3、开始训练模型
# 配置每一个episode结束后要做的事
callbacks = [EarlyStopping(patience=3),
             CSVLogger('cnn_dilation.csv'),
             ModelCheckpoint('cnn_best_dilation.h5', save_best_only=True)]

# 训练数据
train_data = CaptchaSequence(characters, batch_size=128, steps=1000, path='image')
# 测试数据
valid_data = CaptchaSequence(characters, batch_size=128, steps=100, path='image2')

model.fit(train_data,
          epochs=100,
          validation_data=valid_data,
          callbacks=callbacks)
