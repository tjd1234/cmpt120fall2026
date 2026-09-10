# mystery10.py

def count_up(n):
    if n < 1:
        return
    else:
        count_up(n - 1)
        print(n)

print('mystery10.py: calling count_up(5) ...')
count_up(5)
