# mystery5.py

def mystery(n):
    print(f'calling mystery({n}) ...')
    mystery(n)

print('mystery5.py: calling mystery(1) ...')
mystery(75)
