from ..game import board
from ..game import car

import tensorflow as ts
import keras



model = keras.models.Sequential()

model.add(keras.layers.Dense(units=36, activation='relu'))
model.add(keras.layers.Dense(units=72, activation='relu'))
model.add(keras.layers.Dense(units=1, activation='linear'))

