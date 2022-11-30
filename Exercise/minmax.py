# numbers = input('Enter a Sequence of numbers: ')

# x=[int(x) for x in inp.split(" ")]
numbers = [10, 20 , 500, 600 ,8000]
def minmax(data):
    l = data[0]
    s = data[0]
    for num in data:
        if num > l:
            l = num
        elif num < s:
            s = num
            return l, s
    print(s)
    print(l)

minmax(numbers)

