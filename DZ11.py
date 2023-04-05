b = 0
while (b == b):
    x = int(input('Type number x:'))
    y = int(input('Type number y:'))
    o = input('choose operation(+,=,*,/):')
    if o == '+':
        print (x + y)
    elif o == '-':
        print(x - y)
    elif o == '*':
        print(x * y)
    elif o == '/' and y != 0:
        print(x / y)
    else:print('Error')
    a = input('Continue working with calc?(yes or no):')
    a = (a.lower())
    if a != 'yes':
        break
    else:
        continue





