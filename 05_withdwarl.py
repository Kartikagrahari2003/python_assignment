# Q 5. Add and withdrawl money....
initial = 10000 
print(f"Your initial amount is: {initial} Rs")

choose = input("For deposit press 1.....\nFor withdrawal press 2.....")

if choose == "1":
    deposit = float(input("Enter your deposit amount: "))
    initial = deposit + initial
    print(f"Your remaining amount: {initial} Rs")

elif choose == "2":
    withdrawal = float(input("Enter withdrawal amount: "))
    
    if withdrawal > initial:
        print("Insufficient fund....")
    else:
        initial = initial - withdrawal
        print(f"Your remaining balance is: {initial} Rs")

else:
    print("Invalid choice")






