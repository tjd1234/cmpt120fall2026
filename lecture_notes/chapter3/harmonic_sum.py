# harmonic_sum.py

#
# This function prints the sum 1/1 + 1/2 + 1/3 + ... + 1/n, where n is a
# positive integer passed as a parameter.
#

def harmonic_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += 1 / i
    print(sum)

harmonic_sum(10)
