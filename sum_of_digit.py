n = int(input('Enter the number to find sum of digits : '))
add = 0
while n:
    add += n % 10
    n //= 10
print(f'Sum of digits : {add}')