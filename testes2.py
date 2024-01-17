

x = 101
y = 904
palindromo = []
palindromo2 = []
palindromo3 = []
multiplicação = []

# while True:
# x = 999
# x -= 1

while True:
    number = x * y
    number = str(number)
    for i in number[::-1]:
        palindromo2.append(i)
    for index in number:
        palindromo.append(index)
    if palindromo2 == palindromo:
        palindromo3.append(palindromo)
        multiplicação.append(y)
    palindromo = []
    palindromo2 = []
    y += 1
    if y == 999:
        break

# break

print(palindromo3)
print(multiplicação)
