n = int(input('Enter any number to check palyprime or not : '))

dup = n
for den in range(2,n//2 + 1):
    if n % den == 0:
        print('Not palyprime')
        break
else:
    rev = 0
    while dup:
        rev = rev *10 + dup % 10
        dup //= 10
    if rev == n:
        print(f'Palyprime number: {n}')
    else:
        print('Not Palyprime')