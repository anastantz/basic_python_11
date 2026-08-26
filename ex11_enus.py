# Program that calculates the area of a wall and the amount of paint needed

width = float(input("Enter the width of the wall in meters: "))
height = float(input("Enter the height of the wall in meters: "))

area = width * height
paint = area / 2

print(f"Your wall has the dimension of {width}x{height} and its area is {area:.2f}m².")
print(f"To paint this wall, you will need {paint:.2f}l of paint.")