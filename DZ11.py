m = input('Start working with calc?(type "yes" or "no")')
while m == 'yes':
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

    if a == 'yes':
        continue
    else:
        print('End')
else:
    print('End')



