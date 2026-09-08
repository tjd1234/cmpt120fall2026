# mult_table.py


#
# This is the table we want to print:
#
#        1   2   3   4   5   6   7   8   9  10 
#      ----------------------------------------
#   1 |  1   2   3   4   5   6   7   8   9  10 
#   2 |  2   4   6   8  10  12  14  16  18  20 
#   3 |  3   6   9  12  15  18  21  24  27  30 
#   4 |  4   8  12  16  20  24  28  32  36  40 
#   5 |  5  10  15  20  25  30  35  40  45  50 
#   6 |  6  12  18  24  30  36  42  48  54  60 
#   7 |  7  14  21  28  35  42  49  56  63  70 
#   8 |  8  16  24  32  40  48  56  64  72  80 
#   9 |  9  18  27  36  45  54  63  72  81  90 
#  10 | 10  20  30  40  50  60  70  80  90 100 
#

# # version 1
# for row in range(1, 11):
#     for col in range(1, 11):
#         print(f'{row * col}', end=' ')
#     print()

# # version 2: pad with space to make the table look nice
# for row in range(1, 11):
#     for col in range(1, 11):
#         print(f'{row * col:3}', end=' ')
#     print()

# # version 3: add the row number and | at the start of each row
# for row in range(1, 11):
#     print(f'{row:2} |', end='')
#     for col in range(1, 11):
#         print(f'{row * col:3}', end=' ')
#     print()

# version 3: add the top two rows
print('      1   2   3   4   5   6   7   8   9  10 ')
print('    ----------------------------------------')
for row in range(1, 11):
    print(f'{row:2} |', end='')
    for col in range(1, 11):
        print(f'{row * col:3}', end=' ')
    print()
