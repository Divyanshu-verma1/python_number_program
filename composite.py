n = int(input('Enter the number : '))

for digit in range(2,n//2 +1):
    if n % digit == 0:
        print('Composite Number')
        break
else:
    print('Prime number')