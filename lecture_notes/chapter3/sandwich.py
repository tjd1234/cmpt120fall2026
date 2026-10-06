# sandwich.py

def sandwich(text):
    line = '-' * len(text)
    print(line)
    print(text)
    print(line)

text = input('What text do you want to sandwich? ')
sandwich(text)