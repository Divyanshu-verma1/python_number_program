n = int(input('enter any number'))
# first method
if n % 2 == 0:
    print('Even number')
else:
    print('Odd number')

# second method
print('Even number' if n%2 == 0 else 'Odd number')