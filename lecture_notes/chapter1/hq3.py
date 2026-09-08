# hq3.py

# get the information
name = input('What is your name? ')
thing1 = input('What is your first favourite thing? ')
thing2 = input('What is your second favourite thing? ')
thing3 = input('What is your third favourite thing? ')

# generate the web page
print('<html>')
print('<head>')
print(f'<title>{name}\'s Web Page</title>')
print('</head>')
print('<body>')
print(f'<h1>{name}\'s Web Page</h1>')
print(f'<p>Welcome to my web page. I\'m {name}, a student at SFU. Here are a few of my favourite things:</p>')
print('<ul>')
print(f'<li>{thing1}</li>')
print(f'<li>{thing2}</li>')
print(f'<li>{thing3}</li>')
print('</ul>')
print('</body>')
print('</html>')