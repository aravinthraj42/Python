radius = float(input('Enter the radius: '))
import math
# Area of circle
pi = math.pi
areaofcircle = round(pi*radius*2)
print(areaofcircle)
# Area of Rectangle
react = input('Enter the length and breadth of a reactangle separted by space: ')
length = float(react.split()[0])
breadth= float(react.split()[1])
areaofReact = length * breadth
print(areaofReact)

