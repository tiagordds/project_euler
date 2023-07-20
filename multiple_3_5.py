
numbers = []

for n in range(1000):
    if n % 3 == 0:
        numbers.append(n)
    if n % 5 == 0:
        numbers.append(n)
    if len(numbers) >= 2:
        if numbers[-1] == numbers[-2]:
            numbers.pop(-1)

print(sum(numbers))
