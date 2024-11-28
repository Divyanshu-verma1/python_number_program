print('Enter two number to find the GCF : ')
a = int(input('Enter the first number'))
b = int(input('Enter the second number'))

if a > b:
    gcf = b
else:
    gcf = a

while True:
    if a % gcf == 0 and b % gcf == 0:
        print(f'GCF of {a}, {b} is : {gcf}')
        break
    gcf -= 1
    