print('Enter the two number to find the LCM :')
a = int(input('Enter the first number : '))
b = int(input('Enter the second number : '))

if a > b:
    lcm = a
else:
    lcm = b

while True:
    if lcm % a == 0 and lcm % b == 0:
        print(f'LCM od {a} , {b} is : {lcm}')
        break
    lcm += 1
    
