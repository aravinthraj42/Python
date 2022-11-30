num = int(input('Enter a number: '))

def poistive():
    # sum = 0
    small = [i * i for i in range(1, num)]
    # print(i)
    # small = i *i
    # print(small)
    # #sum = sum + small
    square = sum(small)
    # square = num *num
    return square


print("Sum of the square of all positive integers small than given number:", poistive())
