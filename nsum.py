# 1 se N tak sab numbers ka sum find karo
print("Sum of 'N' numbers😊")

x= int(input("Enter the 'N' number:::"))

if x< 0 or x==0:
    print("'N' can't be zero or less than zero....")
    
else:
    y = 0
    for i in range(1, x+1): # stop stopper value ko include nahhi krta...... 
        y = y + i

        print(f"Answer::: {y}")
    
