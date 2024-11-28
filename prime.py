n = int(input('Enter any number to check prime or not : '))

# first method
factor = 0
for digit in range(1,n+1):
    if n % digit == 0:
        factor += 1

if factor == 2:
    print('Prime number')
else:
    print('Not a prime number')

# second method
for digit in range(2,n//2 + 1):
    if n % digit == 0:
        print('Not a prime number')
        break
else:
    print('Prime number')
