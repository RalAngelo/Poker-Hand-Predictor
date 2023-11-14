import tkinter as tk
from tkinter import *
from tkinter import messagebox
import numpy as np
import collections

class PokerHandPredictor(tk.Tk):
    def __init__(self, master = None):
        super().__init__(master)

        self.title("Poker Hand Predictor")
        self.geometry("200x500")
        # Create a label to display the instruction
        self.instruction_label = tk.Label(self, text='Enter the poker hand here:')
        self.instruction_label.place(x=10, y=10)
        self.label_hand = tk.LabelFrame(self, text = "Hand")
        self.label_hand.place(x = 10, y = 400, width = 160 , height = 80)
        # Create the hand entries
        self.hand_entries = []
        titles = ["Card 1: ","Rank 1: " , "Card 2: ","Rank 2: " , "Card 3: ","Rank 3: " , "Card 4: ","Rank 4: " , "Card 5: ","Rank 5: " ,"PokerHand: "]
        for i in range(11):
            entry = tk.Entry(self, width=10)
            tk.Label(self, text=titles[i]).place(x=10, y=80 * ((i * (30/100)) + 1))
            self.hand_entries.append(entry)
            entry.place(x=100 , y=80 * ((i * (30/100)) + 1))

        # Create the predict button
        self.predict_button = tk.Button(self, text='Predict', command=self.predict_hand)
        self.predict_button.place(x=10, y=360)

    def predict_hand(self):
        # Get the values from the entry widgets
        hand_values = []
        for entry in self.hand_entries:
            value = entry.get()
            if value != '':
                try:
                    hand_values.append(int(value))
                except ValueError:
                    show_error_message("Prediction Error", "Please enter valid card or rank values.")
                    return

        # Check the length of the hand values
        if len(hand_values) != 11:
            show_error_message("Prediction Error", "Please enter a valid hand.")
            return

        # Check the card values
        for i in range(0, 10, 2):
            if hand_values[i] < 1 or hand_values[i] > 13:
                show_error_message("Prediction Error", "Please enter valid card values.")
                return

        # Check the rank values
        for i in range(1, 10, 2):
            if hand_values[i] < 1 or hand_values[i] > 4:
                show_error_message("Prediction Error", "Please enter valid rank values.")
                return

        # Check the poker hand value
        if hand_values[10] < 1 or hand_values[10] > 9:
            show_error_message("Prediction Error", "Please enter a valid hand value.")
            return

        hand_array = np.array(hand_values)
        handToTest = hand_array[:-1]

        print(handToTest)
        result = ""
        # Check if the hand is a royal straight flush
        if is_royal_straight_flush(handToTest):
            if hand_values[10] != 9:
                show_error_message("Prediction Error", "It's royal flush the value is 9, Please rectify it")

            # Print the result
            result = "Royal Straight Flush"
        
        if is_straight_flush(handToTest):
            if hand_values[10] != 8:
                show_error_message("Prediction Error", "It's straight_flush the value is 8, Please rectify it")
        
            result = "Straight Flush"
        
        if is_flush(handToTest):
            if hand_values[10] != 5:
                show_error_message("Prediction Error", "It is_flush the value is 5, Please rectify it")
        
            result = "is_flush"

        if is_straight(handToTest):
            if hand_values[10] != 4:
                show_error_message("Prediction Error", "It is_straight the value is 4, Please rectify it")
        
            result = "is_straight"

        result_label = tk.Label(self.label_hand, text = result)
        result_label.pack()
        
        # Print the numpy array
        print(hand_array)

def is_royal_straight_flush(hand):

    if len(set(hand[::2])) != 5:
        return False
    if len(set(hand[1::2])) != 1:
        return False
    if sorted(hand[::2]) != [1, 10, 11, 12, 13]:
        return False

    return True

def is_straight_flush(hand):

    if len(set(hand[1::2])) != 1:
        return False
    ranks = sorted(set(hand[::2]))
    if len(ranks) != 5 or (ranks[-1] - ranks[0]) != 4:
        return False

    return True

def is_flush(hand):
    # Check if all cards are of the same suit
    if len(set(hand[1::2])) != 1:
        return False

    return True


def is_straight(hand):
    # Sort the ranks of the cards
    ranks = sorted(set(hand[::2]))

    # Check if there are five consecutive ranks
    if len(ranks) != 5 or (ranks[-1] - ranks[0]) != 4:
        return False

    return True

def show_error_message(title, message):
    """Displays an error message in an alert window."""
    root = tk.Tk()
    root.withdraw()
    tk.messagebox.showerror(title, message)
    root.mainloop()

if __name__ == '__main__':
    app = PokerHandPredictor()
    app.mainloop()
