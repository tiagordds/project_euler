
square_first_hundred = []
one_hundred = []
x = 0
y = 0
for n in range(11):
    y = n
    one_hundred.append(y)
    x = n ** 2
    square_first_hundred.append(x)

print(square_first_hundred)
print(sum(one_hundred))
z = (sum(one_hundred)) ** 2
print(z)
print( z -  sum(square_first_hundred))