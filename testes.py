
def is_prime(x):
    if x == 3 or x == 2:
        return True
    if x % 2 == 0:
        return False
    y = x / 2
    y = int(y)
    z = x
    while True:
        a = z % y
        if y == 1:
            return True
        if a == 0:
            return False
        y -= 2
        if y <= 0:
            return False
primes = []
x = 100

while True:
    if x == 1:
        break
    if is_prime(x) is True:
        primes.append(x)
    x -= 1

print(primes)