#  Calculate surface area of a cuboid 
print("Calculate surface area of a cuboid 😒")

l = float(input("Enter length of cuboid: "))
b = float(input("Enter breadth of cuboid: "))
h = float(input("Enter height of cuboid: "))

surface_area = 2 * (l*b + b*h + h*l)

print(f"Surface area = {surface_area}")