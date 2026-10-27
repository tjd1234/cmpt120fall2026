# box2.py

def box(text):
    n = len(text)
    print('+-' + '-' * n + '-+')
    print('| ' + text + ' |')
    print('+-' + '-' * n + '-+')

text = input('What text do you want to box? ')
box(text)