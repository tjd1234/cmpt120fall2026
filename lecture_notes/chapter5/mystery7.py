# mystery7.py

def mystery(n):
    if n > 5:
        return
    print(f'calling mystery({n + 1}) ...')
    mystery(n + 1)
    print(f'done with mystery({n + 1})')

print('mystery7.py: calling mystery(1) ...')
mystery(1)
