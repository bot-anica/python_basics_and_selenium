# ---------- TUPLES
print("----- TUPLES -----")

# Tuples are same as lists, but they are immutable
# Tuples are faster than lists
# Tuples are faster than strings
# Tuples are faster than sets

# Tuple methods
# count(item) - counts the number of occurrences of an item in a tuple
# index(item) - returns the index of an item in a tuple
# +(other tuple) - concatenates two tuples
# *(n) - repeats a tuple n times
# len(tuple) - returns the length of a tuple

# Useful example of using Tuples
chess_board_rows = ("a", "b", "c", "d", "e", "f", "g", "h")
chess_board_columns = (1, 2, 3, 4, 5, 6, 7, 8)

chess_board_rows_list = []

for row in chess_board_rows:
    chess_board_row = []

    for column in chess_board_columns:
        chess_board_row.append((row, column))

    chess_board_rows_list.append(chess_board_row)

for row in chess_board_rows_list:
    print(row)
