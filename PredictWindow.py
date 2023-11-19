import tkinter as tk
from tkinter import *
from tkinter import messagebox
import numpy as np
import tensorflow as tf
import math

class PokerHandPredictor(tk.Tk):
    def __init__(self, master = None):
        super().__init__(master)

        self.title("Poker Hand Predictor")
        self.geometry("200x600")
        
        self.instruction_label = tk.Label(self, text='Enter the poker hand here:')
        self.instruction_label.place(x=10, y=10)
        self.label_hand = tk.LabelFrame(self, text = "Hand")
        self.label_hand.place(x = 10, y = 400, width = 160 , height = 80)

        self.label_hand_p = tk.LabelFrame(self, text = "PredictHand")
        self.label_hand_p.place(x = 10, y = 500, width = 160 , height = 80)
        
        self.hand_entries = []
        titles = ["Card 1: ","Rank 1: " , "Card 2: ","Rank 2: " , "Card 3: ","Rank 3: " , "Card 4: ","Rank 4: " , "Card 5: ","Rank 5: " ,"PokerHand: "]
        for i in range(11):
            entry = tk.Entry(self, width=10)
            tk.Label(self, text=titles[i]).place(x=10, y=80 * ((i * (30/100)) + 1))
            self.hand_entries.append(entry)
            entry.place(x=100 , y=80 * ((i * (30/100)) + 1))

        
        self.predict_button = tk.Button(self, text='Predict', command=self.predict_hand)
        self.predict_button.place(x=10, y=360)

    def predict_hand(self):
        
        hand_values = []
        for entry in self.hand_entries:
            value = entry.get()
            if value != '':
                try:
                    hand_values.append(int(value))
                except ValueError:
                    show_error_message("Prediction Error", "Please enter valid card or rank values.")
                    return

        
        if len(hand_values) != 11:
            show_error_message("Prediction Error", "Please enter a valid hand.")
            return

        
        for i in range(0, 10, 2):
            if hand_values[i] < 1 or hand_values[i] > 13:
                show_error_message("Prediction Error", "Please enter valid card values.")
                return

        
        for i in range(1, 10, 2):
            if hand_values[i] < 1 or hand_values[i] > 4:
                show_error_message("Prediction Error", "Please enter valid rank values.")
                return

        
        if hand_values[10] < 0 or hand_values[10] > 9:
            show_error_message("Prediction Error", "Please enter a valid hand value.")
            return

        hand_array = np.array(hand_values)
        handToTest = hand_array[:-1] 

        if has_duplicate_cards(handToTest.reshape(5,2)):
            show_error_message("Prediction error", "Duplicate cards found")
            return

        print(handToTest)
        result = ""

        if is_royal_straight_flush(handToTest.reshape(5, 2)):
            if hand_array[10] != 9:
                show_error_message("Prediction Error", "It's royal flush the value is 9, Please rectify it")
            result = "is_royal_straight_flush"
        
        if is_straight_flush(handToTest.reshape(5, 2)):
            if hand_array[10] != 8:
                show_error_message("Prediction Error", "It is_straight_flush the value is 8, Please rectify it")
            result = "is_straight_flush"
        
        if is_four_of_a_kind(handToTest.reshape(5, 2)):
            if hand_array[10] != 7:
                show_error_message("Prediction Error", "It is four of kind the value is 7, Please rectify it")
            result = "is_four_of_a_kind"
        
        if is_full_house(handToTest.reshape(5, 2)):
            if hand_array[10] != 6:
                show_error_message("Prediction Error", "It's full house the value is 6, Please rectify it")
            result = "is_full_house"

        if is_flush(handToTest.reshape(5, 2)) and not is_royal_straight_flush(handToTest.reshape(5, 2)) and not is_straight_flush(handToTest.reshape(5, 2)):
            if hand_array[10] != 5:
                show_error_message("Prediction Error", "It is_flush the value is 5, Please rectify it")
            result = "is_flush"
        
        if is_straight(handToTest.reshape(5, 2)) and not is_royal_straight_flush(handToTest.reshape(5, 2)) and not is_straight_flush(handToTest.reshape(5, 2)):
            if hand_array[10] != 4:
                show_error_message("Prediction Error", "It's straight the value is 4, Please rectify it")
            result = "is_straight"
        
        if is_three_of_a_kind(handToTest.reshape(5, 2)) and not is_full_house(handToTest.reshape(5, 2)) and not is_four_of_a_kind(handToTest.reshape(5, 2)):
            if hand_array[10] != 3:
                show_error_message("Prediction Error", "It's three the value is 3, Please rectify it")
            result = "three"
        
        if is_two_pair(handToTest.reshape(5, 2)) and not is_four_of_a_kind(handToTest.reshape(5, 2)) and not is_full_house(handToTest.reshape(5, 2)):
            if hand_array[10] != 2:
                show_error_message("Prediction Error", "It's two pair the value is 2, Please rectify it")
            result = "two pairs"
        
        if is_one_pair(handToTest.reshape(5, 2)) and not is_two_pair(handToTest.reshape(5, 2)) and not is_three_of_a_kind(handToTest.reshape(5, 2)) and not is_full_house(handToTest.reshape(5, 2)) and not is_four_of_a_kind:
            if hand_array[10] != 1:
                show_error_message("Prediction Error", "It's royal flush the value is 9, Please rectify it")
            result = "one pair"
        
        if is_high_card(handToTest.reshape(5, 2)) and not is_royal_straight_flush(handToTest.reshape(5, 2)) and not is_straight_flush(handToTest.reshape(5, 2)) and not is_four_of_a_kind(handToTest.reshape(5, 2)) and not is_full_house(handToTest.reshape(5, 2)) and not is_straight(handToTest.reshape(5, 2)) and not is_flush(handToTest.reshape(5, 2)) and not is_three_of_a_kind(handToTest.reshape(5, 2)) and not is_two_pair(handToTest.reshape(5, 2)) and not is_one_pair(handToTest.reshape(5, 2)):
            if hand_array[10] != 0:
                show_error_message("Prediction Error", "It's high card the value is 0, Please rectify it")
            result = "high card"

        result_label = tk.Label(self.label_hand, text = result)
        result_label.pack()

        model = tf.keras.models.load_model('model2.h5')
        prediction = model.predict(hand_array.reshape(1, 11))

        result_p = ""
        hand = ["Royal straigth flush", "Straight flush", "Four of the kind",
                         "Full house", "Flush", "Straight", "Three of the kind",
                          "two pairs", "one pair", "high card"]
        for i in range((10)):
            if math.ceil(prediction) == i:
                result_p = hand[9-i]

        result_label_p = tk.Label(self.label_hand_p, text = result_p)
        result_label_p.pack()

def is_royal_straight_flush(hand):
    cards = hand[:, 0]
    if is_flush(hand) and list(sorted(cards)) == [1, 10, 11, 12, 13]:
        return True
    else:
        return False

def is_straight_flush(hand):
    if is_flush(hand) and is_straight(hand):
        return True
    else:
        return False

def is_flush(hand):
    suits = hand[:, 1]
    if len(set(suits)) != 1:
        return False

    return True

def is_straight(hand):
    cards = hand[:, 0]
    ranks = sorted(cards)

    if len(ranks) != 5 or (ranks[-1] - ranks[0]) != 4:
        return False

    return True

def is_four_of_a_kind(hand):
    ranks = hand[:, 0]
    suits = hand[:, 1]

    rank_counts = np.bincount(ranks)

    if any(count == 4 for count in rank_counts):
        if sum(count == 4 for count in rank_counts) == 1:
            return True
        else:
            return False
    else:
        return False

def is_full_house(hand):
    ranks = hand[:, 0]
    suits = hand[:, 1]

    rank_counts = np.bincount(ranks)

    if any(count == 3 for count in rank_counts) and any(count == 2 for count in rank_counts):
        if sum(count == 3 for count in rank_counts) == 1 and sum(count == 2 for count in rank_counts) == 1:
            return True
        else:
            return False
    else:
        return False

def is_three_of_a_kind(hand):
    ranks = hand[:, 0]
    suits = hand[:, 1]

    rank_counts = np.bincount(ranks)

    if any(count == 3 for count in rank_counts):
        if sum(count == 3 for count in rank_counts) == 1:
            return True
        else:
            return False
    else:
        return False

def is_two_pair(hand):
    ranks = hand[:, 0]
    suits = hand[:, 1]

    rank_counts = np.bincount(ranks)

    if any(count == 2 for count in rank_counts):
        if sum(count == 2 for count in rank_counts) == 2:
            return True
        else:
            return False
    else:
        return False

def is_one_pair(hand):
    ranks = hand[:, 0]
    suits = hand[:, 1]

    rank_counts = np.bincount(ranks)

    if any(count == 2 for count in rank_counts):
        if sum(count == 2 for count in rank_counts) == 1:
            return True
        else:
            return False
    else:
        return False

def is_high_card(hand):
    ranks = hand[:, 0]
    suits = hand[:, 1]

    rank_counts = np.bincount(ranks)

    if not any(count == 2 for count in rank_counts):
        if not any(count == 3 for count in rank_counts):
            if not any(count == 4 for count in rank_counts):
                return True
    else:
        return False

def has_duplicate_cards(hand):
    table_counts = {}

    for table in hand:
        table_str = str(table)

        if table_str in table_counts:
            table_counts[table_str] += 1
        else:
            table_counts[table_str] = 1

    duplicate_count = 0
    for table_str, count in table_counts.items():
        if count > 1:
            duplicate_count += 1

    return duplicate_count

def show_error_message(title, message):
    """Displays an error message in an alert window."""
    root = tk.Tk()
    root.withdraw()
    tk.messagebox.showerror(title, message)
    root.mainloop()

if __name__ == '__main__':
    app = PokerHandPredictor()
    app.mainloop()
