n = int(input('Enter the number to find factorial : '))
dup = n
fact = 1
while n:
    fact *= n
    n -= 1

print(f'Factorial of {dup} is : {fact}')