import numpy as np

array = np.array([[2, 1],
                  [5, 2],
                  [2, 1],
                  [2, 4],
                  [1, 4]])

# Create a dictionary to store the counts of each unique table
table_counts = {}

# Iterate over the array and count the occurrences of each table
for table in array:
    table_str = str(table)
    if table_str in table_counts:
        table_counts[table_str] += 1
    else:
        table_counts[table_str] = 1

# Print the counts of each unique table
for table_str, count in table_counts.items():
    print("The table", table_str, "appears", count, "times in the array.")
