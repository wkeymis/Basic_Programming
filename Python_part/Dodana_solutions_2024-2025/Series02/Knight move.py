start = input()
end = input()

start_col = ord(start[0]) - ord('a') + 1
start_row = int(start[1])
end_col = ord(end[0]) - ord('a') + 1
end_row = int(end[1])

col_diff = abs(start_col - end_col)
row_diff = abs(start_row - end_row)

if (col_diff == 2 and row_diff == 1) or (col_diff == 1 and row_diff == 2):
    print(f"a knight can jump from {start} to {end}")
else:
    print(f"a knight cannot jump from {start} to {end}")