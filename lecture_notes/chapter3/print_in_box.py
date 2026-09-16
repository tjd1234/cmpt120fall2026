# print_in_box.py

#
# This function prints a given word in a box.
#

def box(text):
    n = len(text)
    line = '+-' + '-' * n + '-+'
    print(line)
    print('| ' + text + ' |')
    print(line)

def print_in_boxes(n):
    for i in range(n):
        box(i)

print_in_boxes(4)
