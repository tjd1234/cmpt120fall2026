# box1.py

def box(text):
    print('+-' + '-' * len(text) + '-+')
    print('| ' + text + ' |')
    print('+-' + '-' * len(text) + '-+')

text = input('What text do you want to box? ')
box(text)