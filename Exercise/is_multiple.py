def is_multiple(n, m):
    if (n % m == 0):
        return True
    elif (n % m != 0):
        return False


num1 = int(input('Enter a Number 1 :'))
num2 = int(input('Enter a Number 2: '))

print(is_multiple(num1, num2))
