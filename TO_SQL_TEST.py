import pymysql

# Connect to the database
conn = pymysql.connect(
    host="localhost",
    user="Angelo",
    password="P_ssw0rd"
)

# Create a cursor
cur = conn.cursor()

# Create the database
cur.execute("CREATE DATABASE IF NOT EXISTS PokerTest")

# Use the new database
cur.execute("USE PokerTest")

# Create the table
cur.execute("""CREATE TABLE IF NOT EXISTS poker_hands (
  suit_of_card_1 VARCHAR(255),
  rank_of_card_1 INT,
  suit_of_card_2 VARCHAR(255),
  rank_of_card_2 INT,
  suit_of_card_3 VARCHAR(255),
  rank_of_card_3 INT,
  suit_of_card_4 VARCHAR(255),
  rank_of_card_4 INT,
  suit_of_card_5 VARCHAR(255),
  rank_of_card_5 INT,
  poker_hand INT
)""")

# Import the data from the CSV file into the table
cur.execute(f"""
LOAD DATA INFILE '/var/lib/mysql-files/poker-hand-testing.csv' INTO TABLE poker_hands FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES
""")

# Update the table to convert the suit codes to suit names
cur.execute("""UPDATE poker_hands
SET suit_of_card_1 = CASE WHEN suit_of_card_1 = 1 THEN 'Hearts'
                          WHEN suit_of_card_1 = 2 THEN 'Spades'
                          WHEN suit_of_card_1 = 3 THEN 'Diamonds'
                          ELSE 'Clubs'
                          END,
    suit_of_card_2 = CASE WHEN suit_of_card_2 = 1 THEN 'Hearts'
                          WHEN suit_of_card_2 = 2 THEN 'Spades'
                          WHEN suit_of_card_2 = 3 THEN 'Diamonds'
                          ELSE 'Clubs'
                          END,
    suit_of_card_3 = CASE WHEN suit_of_card_3 = 1 THEN 'Hearts'
                          WHEN suit_of_card_3 = 2 THEN 'Spades'
                          WHEN suit_of_card_3 = 3 THEN 'Diamonds'
                          ELSE 'Clubs'
                          END,
    suit_of_card_4 = CASE WHEN suit_of_card_4 = 1 THEN 'Hearts'
                          WHEN suit_of_card_4 = 2 THEN 'Spades'
                          WHEN suit_of_card_4 = 3 THEN 'Diamonds'
                          ELSE 'Clubs'
                          END,
    suit_of_card_5 = CASE WHEN suit_of_card_5 = 1 THEN 'Hearts'
                          WHEN suit_of_card_5 = 2 THEN 'Spades'
                          WHEN suit_of_card_5 = 3 THEN 'Diamonds'
                          ELSE 'Clubs'
                          END""")

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
