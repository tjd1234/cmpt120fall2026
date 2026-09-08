# mystery4.py

n = 1
def mystery():
    global n # this is necessary to modify the global variable n
    print('calling mystery() again ...')
    n += 1
    print(f'n = {n}')
    mystery()

print('mystery4.py: calling mystery() ...')
mystery()
