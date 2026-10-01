# mystery7.py

def mystery(n):
    if n > 5:
        return
    else:
        print(f'calling mystery({n}) ...')
        mystery(n + 1)

print('mystery7.py: calling mystery(1) ...')
mystery(1)
