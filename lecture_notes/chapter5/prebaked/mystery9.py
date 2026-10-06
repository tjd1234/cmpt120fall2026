# mystery9.py

def count_down(n):
    if n < 1:
        return
    else:
        print(n)
        count_down(n - 1)

print('mystery9.py: calling count_down(5) ...')
count_down(5)
