# Income tax calculator

x = float(input("Enter your monthly income:::"))
y = x*12

if y <= 1200000:
    tax = 0
    print(f"You are safe... your annual income is {y}...")
    print(f"Your tax is {tax}")

elif y >= 1200000:
    tax = y * 0.05
    print(f"You are not safe.... Your annual income is {y}...")
    print(f"your payable tax is {tax}")



