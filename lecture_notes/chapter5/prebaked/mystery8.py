# mystery8.py

def mystery(n):
    if n < 1:
        return
    else:
        print(f"calling mystery({n}) ...")
        mystery(n - 1)


print("mystery8.py: calling mystery(5) ...")
mystery(5)
