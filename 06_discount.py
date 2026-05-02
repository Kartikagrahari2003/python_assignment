# Q 8. find 20% discount at cost price...
print("We have 20% discount on product:::::")
initial = 0
items= int(input("Please enter number of products:::"))
for i in range(items):
    x= float(input("Enter price::::"))
    initial=initial+x
 
print(f"Your total ammount is {initial}")
# after 20% discount 
final= (initial*80)/100
print(f"Fianal payable amount:::{final}") 
    



