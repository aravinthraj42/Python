n = int(input('Enter the number: '))


def find(n):
    sum = 0
    for num in range(1, n + 1):
        sum = sum + num  # 0+1,1+2,3+2
    avg = float(sum / n)
    print(sum)
    return avg

print('Average of ', n, '=', find(n))
