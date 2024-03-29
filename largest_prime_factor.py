import time
start_time = time.time()


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
        y -= 1
        if y == 1:
            return True
        if a == 0:
            return False


primes = []
x = 12999
place_holder_x = x

while True:
    if x == 1:
        break
    if is_prime(x) is True:
        primes.append(x)
    x -= 1


timer = 'prime_timer.txt'

print(len(primes))

with open(timer, 'a', encoding='utf8') as arquivo:
    arquivo.write(f"When x = {place_holder_x} the time is %s seconds\n" %
                  (time.time() - start_time))
