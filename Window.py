import tkinter as tk
import numpy as np
import keras.models

class PokerHandPredictionGUI:
    def __init__(self, model):
        self.model = model

        self.root = tk.Tk()
        self.root.title('Poker Hand Prediction')

        # Create a label for the poker hand input
        self.poker_hand_label = tk.Label(self.root, text='Poker hand:')
        self.poker_hand_entry = tk.Entry(self.root)

        # Create a button to predict the poker hand
        self.predict_button = tk.Button(self.root, text='Predict', command=self.predict_poker_hand)

        # Create a label for the prediction output
        self.prediction_label = tk.Label(self.root, text='Predicted poker hand:')
        self.prediction_entry = tk.Entry(self.root)

        # Place the widgets on the window
        self.poker_hand_label.grid(row=0, column=0)
        self.poker_hand_entry.grid(row=0, column=1)
        self.predict_button.grid(row=1, column=0)
        self.prediction_label.grid(row=2, column=0)
        self.prediction_entry.grid(row=2, column=1)

        self.root.mainloop()

    def predict_poker_hand(self):
        # Get the poker hand input from the user
        poker_hand = self.poker_hand_entry.get()

        # Make a prediction
        prediction = self.model.predict(np.array([poker_hand]))[0][0]

        # Set the prediction output label
        self.prediction_entry.delete(0, 'end')
        self.prediction_entry.insert(0, prediction)

model = keras.models.load_model('model.h5')
# Create the GUI
gui = PokerHandPredictionGUI(model)
