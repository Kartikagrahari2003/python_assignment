# Calculate percentage change

x = float(input("Enter first number:::"))
y = float(input("Enter final number:::"))
#  Formula of percentage change
if x <= y:
    a = (y-x)/x*100
    print(f"Your percentage profit change is {a}%")
elif x >= y:
    a = (y-x)/x *100
    print(f"Your percentage loss change is {a}%")


