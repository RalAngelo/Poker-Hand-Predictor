import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
import keras.models

PokerHandData = pd.read_csv("poker-hand-training.csv")
TOnumpy = PokerHandData.to_numpy()

X_train = TOnumpy.reshape((TOnumpy.shape[0], 11))
poker_hand_column = X_train[:, 10]

Y_train = poker_hand_column.reshape(-1,1)

modele = Sequential()
p = 10
modele.add(Dense(p, input_dim=11, activation='relu'))
modele.add(Dense(p, activation='relu'))
modele.add(Dense(p, activation='relu'))
modele.add(Dense(1, activation='linear'))

mysgd = optimizers.SGD(lr=0.01)
modele.compile(loss='mean_squared_error', optimizer=mysgd)
print(modele.summary())

for k in range(1000):
    loss = modele.train_on_batch(X_train, Y_train)
    print('Erreur :',loss)

PokerHandTestingData = pd.read_csv("poker-hand-testing.csv")
TOnumpyTesting = PokerHandTestingData.to_numpy()

X_test = TOnumpyTesting.reshape((TOnumpyTesting.shape[0], 11))
poker_hand_column_test = X_test[:, 10]
Y_test = poker_hand_column_test.reshape(-1,1)

modele.evaluate(X_test, Y_test)
keras.models.save_model(modele, 'model.h5')