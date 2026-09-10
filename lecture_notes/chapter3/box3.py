# box3.py

def box(text):
    n = len(text)
    line = '+-' + '-' * n + '-+'
    print(line)
    print('| ' + text + ' |')
    print(line)

text = input('What text do you want to box? ')
box(text)