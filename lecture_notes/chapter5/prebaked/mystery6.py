# mystery6.py

def mystery(n):
    print(f'calling mystery({n}) ...')
    mystery(n + 1)

print('mystery6.py: calling mystery(1) ...')
mystery(1)
