
x = 0
y = 0
fibonnaci = [1, 2]
while True:
    x = fibonnaci[-1] + fibonnaci[-2]
    fibonnaci.append(x)
    if sum(fibonnaci) >= 4000000:
       y = fibonnaci[-1] + fibonnaci[-2]
       fibonnaci.append(y)
       break

fibonnaci_even = []
for n in fibonnaci:
    if n % 2 == 0:
        fibonnaci_even.append(n)

print(sum(fibonnaci_even))
