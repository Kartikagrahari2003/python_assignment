# Simplify expression:
# Cheated from gpt (impot cmath)
import cmath

print("If your question is 'ax2+bx+c=0' form😊")
a = int(input("Enter the value of a = "))
b = int(input("Enter the value of b = "))
c = int(input("Enter the value of c = "))

# formula of real/imagenary and equal values.....
# Nature of roots
d= (b**2)- 4*a*c
if d > 0:
    print("roots real and distinct")
elif d < 0:
    print("Roots imaginary")
else:
    print("Roots real and equal")

x1= (-b + cmath.sqrt(d))/(2*a)
x2= (-b - cmath.sqrt(d))/(2*a)

print(f"x1 = {x1}")
print(f"x2 = {x2}")
