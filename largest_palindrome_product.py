
x = 81
y = 89
palindrome = ''

palindrome = str(x * y)

palindrome2 = []
palindrome3 = []

for i in palindrome[::-1]:
    palindrome2.append(i)
for i in palindrome:
    palindrome3.append(i)

if palindrome3 == palindrome2:
    print('TA CERTO RAPAZ')
else:
    print('ERROU')