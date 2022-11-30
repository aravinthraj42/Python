num = int(input('Enter a number: '))



def poistive():
    sum = 0
    for i in range(1, num):
       # print(i)
        small = i * i
        # print(small)
        sum = sum + small
        # sqaure = num *num
    return sum


print("Summ of the square of all poistive integers smallr than given number:", poistive())
