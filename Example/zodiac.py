def findZodiac(year):
    if year % 12 == 1:
        return 'Roaster'
    elif year % 12 == 2:
        return 'Dog'
    elif year % 12 == 3:
        return 'Pig'
    elif year % 12 == 4:
        return 'Rat'
    elif year % 12 == 5:
        return 'Ox'
    elif year % 12 == 6:
        return 'Tiger'
    elif year % 12 == 7:
        return 'Hare'
    elif year % 12 == 8:
        return 'Dragon'
    elif year % 12 == 9:
        return 'Snake'
    elif year % 12 == 10:
        return 'Horse'
    elif year % 12 == 11:
        return 'Sheep'
    elif year % 12 == 0:
        return 'Monkey'


while True:
    year = int(input('Enter  your year of birth: '))
    print('You are born in year:', year)
    print('Your Chinese Zodiac Animal is: ', findZodiac(year))
    ch = input('Enter Y to Continue and N to exit: ')
    if ch == 'n' or ch == 'N':
        print('You opted to exit')
        break
