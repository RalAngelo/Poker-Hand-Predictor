import numpy as np

def is_four_of_a_kind(hand):
    ranks = hand[:, 0]
    suits = hand[:, 1]

    rank_counts = np.bincount(ranks)

    if any(count == 4 for count in rank_counts):
        return True
    else:
        return False

hand = np.array([2, 1, 5, 2, 2, 3, 2, 4, 1, 4])
hand1 = hand.reshape(5, 2)
print(hand1)

if is_four_of_a_kind(hand1):
    print("four of a kind.")
else:
    print("not a four of a kind.")



























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


# Example usage
hand2 = np.array([2, 1, 2, 2, 2, 3, 2, 4, 2, 1])
hand3 = hand2.reshape(5,2)
print(hand3)
print(has_duplicate_cards(hand3))

if has_duplicate_cards(hand3):
    print("Duplicate cards found in hand!")
else:
    print("No duplicate cards found in hand.")




