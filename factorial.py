# Factorial calculator
print("Factorial calculator😊")
x=int(input("Enter the number:::"))

if x <= 0:
    print ("Negetive number ka factorial nahi hota........ Try again")
else:
    fact= 1
    for i in range(1, x+1):#  # start , stop and end...counting start with 0
        fact = fact * i

print(f"Factorial: {fact}")