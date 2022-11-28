def is_even(n):
    return (n & 1);
    # if(k%2 == 0): return True


number = int(input('Enter a Number: '));

if(is_even(number) == 0):
    print(True)
elif(is_even(number) != 0):
    print(False)
