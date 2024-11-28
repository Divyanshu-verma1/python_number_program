n = int(input('Enter the number of fibonacci series required : '))
f = 0
s = 1
for ind in range(n):
    if ind < 2:
        print(ind, end='  ')
    else:
        print(f+s, end='  ')
        f, s = s, f+s

        