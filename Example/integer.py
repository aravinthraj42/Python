numbers = input('enter a list of numbers separted by space: ')
num = numbers.split()
print(num)
sum = 0
for n in num:
    try:
        intnum = int(n)
        print(intnum)
        sum = sum + intnum

    except ValueError:
        print('Entry counld not be convereted to integer, Not valid', n)
print('sum of the valid integer numbers: ', sum)
