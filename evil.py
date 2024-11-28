n = int(input('Enter the number to check evil or odeus number : '))
count = 0
dup = n
while n:
    if n % 2 == 1:
        count += 1
    n //= 2
if count % 2 == 0:
    print(f'Evil number: {dup}')
else:
    print(f'Odeus number: {dup}')