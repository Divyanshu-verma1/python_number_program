n = int(input('Enter the number to find it reverse : '))
rev = 0
while n:
    rev = rev * 10 + n %10
    n //= 10
print(f'Reverse of given number is : {rev}')