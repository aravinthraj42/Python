# import math
# num = int(input('Enter the number: '))
#
# prime = True
# x = int(math.sqrt(num))
# print(x)
# while x > 1:
#     if num % x == 0:
#         print(num % x)
#         print(x, 'divides', num)
#         prime = False
#         break
#     x -= 1
# if prime:
#     print('The number', num, 'is Prime')
# else:
#     print('The number', num, 'is NOT Prime')

num = int(input('Enter the number: '))
prime = True
if num > 1:
    for x in range(2, num + 1):
        if (num % x) == 0:
            print(x, 'divides', num)
            prime = False
            break
if prime:
    print('The number', num, 'is Prime')
else:
    print('The number', num, 'is NOT Prime')
