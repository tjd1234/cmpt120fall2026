# hq3.py

#
# Question 3
# Print exactly this on the screen:
#
# \n \t \\ \' \" are escape characters
#
print('Question 3')
print()

print('Solution 1: multiple print statements')
# get the information
name = 'Anita'
thing1 = 'Programming'
thing2 = 'Bowling'
thing3 = 'Traveling'

# generate the web page
print("<html>")
print("<head>")
print(f"<title>{name}'s Web Page</title>")
print("</head>")
print("<body>")
print(f"<h1>{name}'s Web Page</h1>")
print(f"<p>Welcome to my web page. I'm {name}, a student at SFU. Here are a few of my favourite things:</p>")
print("<ul>")
print(f"<li>{thing1}</li>")
print(f"<li>{thing2}</li>")
print(f"<li>{thing3}</li>")
print("</ul>")
print("</body>")
print("</html>")

print('Solution 2: single triple-quoted f-string')
print()
# get the information
name = 'Anita'
thing1 = 'Programming'
thing2 = 'Bowling'
thing3 = 'Traveling'

# generate the web page
print(f"""<html>
<head>
<title>{name}'s Web Page</title>
</head>

<body>
<h1>{name}'s Web Page</h1>

<p>Welcome to my web page. I'm {name}, a student at SFU. Here are a few of my favourite things:</p>

<ul>
<li>{thing1}</li>
<li>{thing2}</li>
<li>{thing3}</li>
</ul>

</body>
</html>""")
